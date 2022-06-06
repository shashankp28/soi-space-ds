import streamlit as st
import pandas as pd
from services.multiapp import MultiApp
from functools import partial
from pages import show, analysis, help, custom, download, three_d


def refresh():
    pass


file = st.file_uploader('Upload CSV file',
                        type='csv', help="Format")
if file is not None:
    # verification
    st.button("Refresh", on_click=refresh)
    data = pd.read_csv(file)
    app = MultiApp()
    app.add_app('Show data', partial(show.app, data))
    app.add_app('Analysis', analysis.app)
    app.add_app('Custom Plots', custom.app)
    app.add_app('3-D Plots', three_d.app)
    app.add_app('Download', download.app)
    app.add_app('Help', help.app)
    app.run()
