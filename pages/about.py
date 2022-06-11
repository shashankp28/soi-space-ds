from PIL import Image
import streamlit as st


def app():
    st.header('About Us')
    st.subheader('Team Details')

    col1, col2, col3 = st.columns(3)
    original = Image.open('./images/1.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col1.image(original, use_column_width=True)
    original = Image.open('./images/2.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col2.image(original, use_column_width=True)
    original = Image.open('./images/3.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col3.image(original, use_column_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        expander = st.expander("Details")
        expander.write("""
            Shashank P\n
            Contact: 200010048@iitdh.ac.in
        """)
    with col2:
        expander = st.expander("Details")
        expander.write("""
            Anand Hegde\n
            200020007@iitdh.ac.in
        """)
    with col3:
        expander = st.expander("Details")
        expander.write("""
            Arvind Kumar M\n
            200020008@iitdh.ac.in
        """)
    col1, col2, col3 = st.columns(3)
    original = Image.open('./images/4.jpeg')
    original = original.resize((300, 450), Image.ANTIALIAS)
    col1.image(original, use_column_width=True)
    original = Image.open('./images/5.jpeg')
    original = original.resize((300, 450), Image.ANTIALIAS)
    col2.image(original, use_column_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        expander = st.expander("Details")
        expander.write("""
            Harrithha B\n
            200010018@iitdh.ac.in
        """)
    with col2:
        expander = st.expander("Details")
        expander.write("""
           Kavali Sri Vyshnavi Devi\n
           200010023@iitdh.ac.in
        """)
