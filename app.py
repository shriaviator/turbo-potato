import pandas as pd
import streamlit as st
from func_module import generate_chart, mask_list, check_password

if check_password():
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
    # chart = alt.Chart(req_df).mark_point().encode(
    #     x=alt.X('name:N', sort='-y', axis=alt.Axis(title='Name of Instructor')),
    #     y=alt.Y('visits', axis=alt.Axis(title='Number of Days Visited')),

    #     color=alt.Color('status:N', scale=alt.Scale(
    #         domain=domain, range=range_), legend=None),
    #     shape=alt.Shape('status', legend=None),
    #     tooltip=['name', 'visits']
    # ).interactive()

    st.write("###  Num  of days Discourse visited by Staff")
    st.altair_chart(generate_chart(req_df, "visits"),
                    use_container_width=True)
    st.write("###  No  of Topics Viewed by Staff")
    st.altair_chart(generate_chart(req_df, "topics_viewed"),
                    use_container_width=True)
    st.write("###  No  of Posts Read by Staff")
    st.altair_chart(generate_chart(req_df, "posts_read"),
                    use_container_width=True)
    st.write("###  No  of Posts Created by Staff")
    st.altair_chart(generate_chart(req_df, "posts_created"),
                    use_container_width=True)
    st.write("###  No  of Topics Created by Staff")
    st.altair_chart(generate_chart(req_df, "topics_created"),
                    use_container_width=True)
    st.write("###  No  of  Likes Given by Staff")
    st.altair_chart(generate_chart(req_df, "likes_given"),
                    use_container_width=True)
    st.write("###  No  of Likes Received by Staff")
    st.altair_chart(generate_chart(req_df, "likes_received"),
                    use_container_width=True)
