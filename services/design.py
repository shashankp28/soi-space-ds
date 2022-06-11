import base64
import streamlit as st
import json
import pandas as pd


def refresh():
    pass


def show_format(file_dir):
    with open(file_dir, "r") as f:
        format = json.load(f)
    format_data = pd.DataFrame.from_dict(format)
    st.header("Format")
    st.markdown("### Please uplaod a CSV file in the following format")
    st.dataframe(format_data)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
