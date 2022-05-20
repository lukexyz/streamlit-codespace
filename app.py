import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

# ------------------------------------------------------
st.header('Editable Dataframes')

@st.cache
def data_download():
    df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
    return df
df = data_download()

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)
gd.configure_selection(selection_mode="multiple", use_checkbox=True)

gridoptions = gd.build()
grid_table = AgGrid(
    df,
    gridOptions=gridoptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    height=500,
    theme="material", # or "fresh"
    allow_unsafe_jscode=True,
)

sel_row = grid_table["selected_rows"]
df_sel_row = pd.DataFrame(sel_row)

# ------------------------------------------------------
st.header('Counter Example')

if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1
st.write(st.session_state.count)

# ------------------------------------------------------
st.header('Mirror using Session State')
# https://blog.streamlit.io/session-state-for-streamlit/

def update_first():
    st.session_state.second = st.session_state.first

def update_second():
    st.session_state.first = st.session_state.second

st.text_input(label='Textbox 1', key='first', on_change=update_first)
st.text_input(label='Textbox 2', key='second', on_change=update_second)
