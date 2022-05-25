import streamlit as st
from .get_df import to_df


def app(data):
    # data = to_df(file)
    st.dataframe(data)
    st.write('Columns present are ', data.columns.tolist())
