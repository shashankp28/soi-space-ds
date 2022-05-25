import pandas as pd
import streamlit as st
from PIL import Image

rad = st.sidebar.radio("", ['Home', 'About Us', 'Services', 'Team'])
image = Image.open('astronaut.gif')
if rad == 'Home':
    st.image(image)
if rad == "Services":
    file = st.file_uploader('Upload csv file', type='csv')
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)
        st.write('Columns present are ', df.columns.tolist())

        st.header('Select from the box given below to plot the graphs')
        X = st.radio('X-axis', df.columns.tolist())

        Y = st.multiselect('Y-axis', df.columns.tolist()+['All'])
        if 'All' in Y:
            Y = df.columns.tolist()
        # for i in Y:
            # print(df[i])
            # st.line_chart(Y,X)4
