import streamlit as st
from plots import create_plot

col1, col2 = st.columns(2)
all_fig = create_plot(6)

with col1:
    for i in range(3):
        st.pyplot(all_fig[i])
        st.write("Figure1")

with col2:
    for i in range(3, 6):
        st.pyplot(all_fig[i])
