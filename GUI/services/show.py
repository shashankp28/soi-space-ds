import streamlit as st


def app(data):
    st.dataframe(data)
    st.write('Columns present are ', data.columns.tolist())
