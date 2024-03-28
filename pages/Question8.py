import streamlit as st
from streamlit.runtime.state import get_session_state


def main():
    session_state = get_session_state()
    common_list = session_state.common_list

    col1, col2, col3 = st.columns([1, 50, 1])
    with col2:
        st.header('''Consider yourself the leader of an important project but your subordinated are not cooperating with you and not following your instructions seriously. What would be your approach?''')
        text_input = st.text_input("Your Answer")

    # Button to move to Question 2
    with col2:
        if st.button("Move to Predictions"):
            common_list.append(text_input)
            session_state.common_list = common_list
            st.switch_page('pages/Prediction.py')


if __name__ == "__main__":
    main()