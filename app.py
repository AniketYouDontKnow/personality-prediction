import streamlit as st
from streamlit.runtime.state import get_session_state


def main():

    session_state = get_session_state()
    session_state.common_list = []

    st.title("Personality Prediction App")

    st.image('demo.jpg')

    if st.button('Ready to Answer Question 1'):
        st.switch_page('pages/Question1.py')


if __name__ == "__main__":
    main()
