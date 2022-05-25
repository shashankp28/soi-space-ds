import streamlit as st


class MultiApp:
    def __init__(self):
        self.apps = []
        self.titles = []

    def num_apps(self):
        return len(self.apps)

    def add_app(self, title, func):
        self.apps.append(func)
        self.titles.append(title)

    def get_index(self, title):
        return self.titles.index(title)

    def run(self):
        app = st.selectbox(
            'Navigation',
            self.titles)

        self.apps[self.get_index(app)]()
