import pandas as pd


def some():
    return 0


class Some():
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        x = [pd.DataFrame([1, 2, 3])]
        app = {
            "title": title,
            "function": func,
            "args": x
        }
        self.apps.append(app)


app = Some()
app.add_app("hello", some)
print(app.apps)
