import streamlit as st


def app(data):
    st.header('Select from the box given below to plot the graphs')
    X = st.radio('X-axis', data.columns.tolist())

    Y = st.multiselect('Y-axis', data.columns.tolist()+['All'])
    if 'All' in Y:
        Y = data.columns.tolist()
