from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from multiapp import MultiApp
from functools import partial
from services import show, plot

rad = st.sidebar.radio("Tool or Help", ['Tool', 'Help'])

data = None


def refresh():
    rad = "Tool"


if rad == "Tool":
    file = st.file_uploader('Upload CSV file',
                            type='csv', help="Format")
    if file is not None:
        st.button("Refresh", on_click=refresh)
        data = pd.read_csv(file)
        app = MultiApp()
        app.add_app('Show data', partial(show.app, data))
        app.add_app('Plot data', partial(plot.app, data))
        app.run()

if rad == "Help":
    st.header("For now this is help")
