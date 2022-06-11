from PIL import Image
import streamlit.components.v1 as components


def app():
    with open("./components/about.html", "r") as f:
        components.html(f.read(), height=1000000)
