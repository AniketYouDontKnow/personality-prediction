import streamlit as st
from streamlit.runtime.state import get_session_state


def main():
    session_state = get_session_state()
    common_list = session_state.common_list

    col1, col2, col3 = st.columns([1, 50, 1])
    with col2:
        st.title("When you encounter an unknown problem, do you rely on facts or try to generate new possibilities? Explain.")
        text_input = st.text_input("Your Answer")


    with col2:
        if st.button("Move to Question 4"):
            common_list.append(text_input)
            session_state.common_list = common_list
            st.switch_page('pages/Question4.py')


if __name__ == "__main__":
    main()