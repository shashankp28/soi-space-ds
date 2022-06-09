import streamlit as st
import pandas as pd
from services.services import check_format
from services.multiapp import MultiApp
from functools import partial
from pages import show, analysis, help, custom, download, three_d


def refresh():
    pass


st.set_page_config(page_title='Kepler', page_icon='components/favicon.jpg')

file = st.file_uploader('Upload CSV file',
                        type='csv', help="Please refer below for the format of CSV file.")
if file:
    # verification
    # Prediction
    st.button("Refresh", on_click=refresh)
    data = pd.read_csv(file)
    format_status, error_msg = check_format(data)
    if(format_status):
        app = MultiApp()
        app.add_app('Show data', partial(show.app, data))
        app.add_app('Analysis', analysis.app)
        app.add_app('Custom Plots', custom.app)
        app.add_app('3-D Plots', partial(three_d.app, data))
        app.add_app('Download', partial(download.app, data, file.name))
        app.add_app('Help', help.app)
        app.run()
    else:
        st.write(error_msg)
else:
    st.write("Format to be uploaded")
    # @Arvind
