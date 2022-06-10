import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as pgo


def app(df, a, n, alpha):
    df = pd.DataFrame(np.random.randn(10, 5),
                      columns=('col %d' % i
                               for i in range(5)))

    st.line_chart(df)
    st.bar_chart(df)

    countries = ['a', 'b', 'c']
    values = [100, 200, 150]

    fig = pgo.Figure(pgo.Pie(labels=countries, values=values,
                             hoverinfo='label+percent', textinfo='value'))

    st.plotly_chart(fig)
