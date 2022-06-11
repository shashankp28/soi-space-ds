from PIL import Image
import streamlit as st


def app():
    st.header('About Us')
    st.markdown("<p style='text-align: justify;'> simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<p>", unsafe_allow_html=True)

    st.subheader('Team Details')

    col1, col2, col3 = st.columns(3)
    original = Image.open('1.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col1.image(original, use_column_width=True)
    original = Image.open('2.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col2.image(original, use_column_width=True)
    original = Image.open('4.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col3.image(original, use_column_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        expander = st.expander("See explanation")
        expander.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
    with col2:
        expander = st.expander("See explanation")
        expander.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
    with col3:
        expander = st.expander("See explanation")
        expander.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
    col1, col2,col3 = st.columns(3)
    original = Image.open('4.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col1.image(original, use_column_width=True)
    original = Image.open('5.jpeg')
    original = original.resize((200, 250), Image.ANTIALIAS)
    col2.image(original, use_column_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        expander = st.expander("See explanation")
        expander.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
    with col2:
        expander = st.expander("See explanation")
        expander.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)

