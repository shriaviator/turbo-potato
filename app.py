import pandas as pd
import altair as alt
import streamlit as st
from func_module import mask_list


df = pd.read_csv('disc_instructor.csv')
selected_options = st.sidebar.multiselect(
    "Select Instructor", df['name'].tolist()
)
# print(type(selected_options))
req_df = mask_list(df, selected_options)
# this is done as to resolve bug
# str_df = req_df.astype(str)
domain = [True, False]
range_ = ['red', 'green']
chart = alt.Chart(req_df).mark_point().encode(
    x=alt.X('name:N', sort='-y'),
    y=alt.Y('visits'),
    color=alt.Color('status:N', scale=alt.Scale(domain=domain, range=range_)),
    tooltip=['name', 'visits']
)


st.altair_chart(chart, use_container_width=True)
