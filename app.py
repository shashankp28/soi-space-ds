import streamlit as st
import pandas as pd
from services.design import *
from services.services import *
from services.multiapp import MultiApp
from functools import partial
from pages import show, analysis, help, custom, download, three_d, about


st.set_page_config(page_title='Kepler', page_icon='images/favicon.jpg')
set_background('images/background.png')

file = st.file_uploader('Upload CSV file',
                        type='csv', help="Please refer below for the format of CSV file.")
if file:
    st.button("Refresh", on_click=refresh)
    data = pd.read_csv(file)
    format_status, error_msg = check_format(data)
    if(format_status):
        data = predict(data)
        app = MultiApp()
        app.add_app('Show data', partial(show.app, data))
        app.add_app('Analysis', analysis.app)
        app.add_app('Custom Plots', partial(custom.app,data))
        app.add_app('3-D Plots', partial(three_d.app, data))
        app.add_app('Download', partial(download.app, data, file.name))
        app.add_app('About Us', about.app)
        app.add_app('Help', help.app)
        app.run()
    else:
        err = '<p style="font-family:Courier; color:Red; font-size: 20px;">' + \
            error_msg+': Please follow the format</p>'
        st.markdown(err, unsafe_allow_html=True)
        show_format("services/format.json")
else:
    show_format("services/format.json")
