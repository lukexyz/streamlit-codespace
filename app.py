import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title="Streamlit Codespace", page_icon="💎", layout="centered")

# ------------------------------------------------------
st.header('💾 Edit Dataframe')

@st.cache
def data_download():
    df = pd.DataFrame( {'Location': ['London', 'Auckland'], 
                        'Weather': [21, 18], 
                        'Mood': ['☀️', '🌝']})
    return df

df = data_download()
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_default_column(editable=True)
gd.configure_selection(selection_mode="multiple", use_checkbox=True)

gridoptions = gd.build()
grid_table = AgGrid(
    df,
    gridOptions=gridoptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    height=180,
    theme="material", # or "fresh"
    allow_unsafe_jscode=True,
)

st.metric("Weather", value=f"{df.Weather.max()}°C", delta="1.2 °C")


@st.experimental_memo
def save_data(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    df.to_csv("db.csv")
    
if st.button('Apply'):
    save_data(df)
    st.text('Hi')

st.write(pd.DataFrame(grid_table["data"]))
st.write(pd.DataFrame(grid_table["selected_rows"]))

# ====================== PART 2 ======================

st.header('🧮 Session Variables')

if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1
st.write(st.session_state.count)

# ====================== PART 3 ======================

st.header('♾️ Mirror Input')
# https://blog.streamlit.io/session-state-for-streamlit/

def update_first():
    st.session_state.second = st.session_state.first

def update_second():
    st.session_state.first = st.session_state.second

st.text_input(label='Textbox 1', key='first', on_change=update_first)
st.text_input(label='Textbox 2', key='second', on_change=update_second)

# ====================== PART 4 ======================

st.header('🌐 Query Params')
st.markdown('''Append to URL
`?user=luke&id=123`''')

st.write(st.experimental_get_query_params())

username = st.experimental_get_query_params()['user'][0]
userid = st.experimental_get_query_params()['id'][0]

st.write(f'Hello **{username} {userid}**, how are you?')
