import streamlit as st


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
