import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

# ------------------------------------------------------
st.header('📝 Edit Dataframe')

@st.cache
def data_download():
    df = pd.DataFrame( {'Location': ['London', 'Auckland'], 
                        'Weather': [21, 18], 
                        'Mood': ['☀️', '🌝']})
    return df

df = data_download()
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_default_column(editable=True)

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

# ------------------------------------------------------
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

# ------------------------------------------------------
st.header('♾️ Mirror Input')
# https://blog.streamlit.io/session-state-for-streamlit/

def update_first():
    st.session_state.second = st.session_state.first

def update_second():
    st.session_state.first = st.session_state.second

st.text_input(label='Textbox 1', key='first', on_change=update_first)
st.text_input(label='Textbox 2', key='second', on_change=update_second)
