import streamlit as st


def app(data):
    st.dataframe(data)
    st.write('Columns present are ', data.columns.tolist())
    columns = st.multiselect('Columns', data.columns.tolist()+['All'])

    if 'All' in columns:
        columns = data.columns.tolist()

    st.write('No.of rows present are',data.shape[0])
    customized_data = data[columns]
    start = st.number_input("Select start row",step=1,min_value=1,max_value=data.shape[0])
    end = st.number_input("Select end row",step=1,min_value=1,max_value=data.shape[0])
    customized_data = customized_data.iloc[start-1:end]
    st.dataframe(customized_data)
