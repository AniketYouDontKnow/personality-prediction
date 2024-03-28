import streamlit as st
from streamlit.runtime.state import get_session_state


def main():

    session_state = get_session_state()
    common_list = session_state.common_list

    # Center-align the text input box
    col1, col2, col3 = st.columns([1, 50, 1])
    with col2:
        st.title("You joined a new company and it's your first day there.No one seems interested in helping or starting conversation with you. You will ?")
        text_input = st.text_input("Your Answer")

    # Button to move to Question 2
    with col2:
        if st.button("Move to Question 2"):
            common_list.append(text_input)
            session_state.common_list = common_list
            st.switch_page('pages/Question2.py')


if __name__ == "__main__":
    main()
