import streamlit as st
from .get_df import to_df


def app(data):
    # data = to_df(file)
    st.header('Select from the box given below to plot the graphs')
    X = st.radio('X-axis', data.columns.tolist())

    Y = st.multiselect('Y-axis', data.columns.tolist()+['All'])
    if 'All' in Y:
        Y = data.columns.tolist()
