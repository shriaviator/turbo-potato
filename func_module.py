import streamlit as st
import altair as alt


def mask_list(df, maskname):
    """
    -[] edge cases all and none 


    Args:
        df (_type_): _description_
        maskname (_type_): _description_

    Returns:
        _type_: _description_
    """
    tempdf = df.copy(deep=True)
    final_list = []
    for loc, xray in enumerate(tempdf['name'].tolist()):
        if xray in maskname:
            final_list.append(xray)
        else:
            final_list.append("i" + str(loc))

    tempdf['name'] = final_list
    mask = tempdf.name.apply(lambda x: any(
        item for item in maskname if item == x))
    tempdf['status'] = mask
    return tempdf


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


def generate_chart(req_df, chart_param):
    yaxis_title = {
        "visits": "No of Days Visited",
        "topics_viewed": "No of Topics Viewed",
        "posts_read": "No of Posts Read",
        "posts_created": "No of Posts Created",
        "topics_created": "No of Topics Created",
        "likes_given": "No of Likes Given",
        "likes_received": "No of Likes received",




    }
    domain = [True, False]
    range_ = ['red', 'green']
    scatter_chart = alt.Chart(req_df).mark_point().encode(
        x=alt.X('name:N', sort='-y', axis=alt.Axis(title='Name of Instructor')),
        y=alt.Y(chart_param, axis=alt.Axis(title=yaxis_title[chart_param])),



        color=alt.Color('status:N', scale=alt.Scale(
            domain=domain, range=range_), legend=None),
        shape=alt.Shape('status', legend=None),
        tooltip=['name', chart_param]
    ).interactive()
    return scatter_chart


# visits	topics_viewed	posts_read	posts_created	topics_created	topics_with_replies	likes_given	likes_received
