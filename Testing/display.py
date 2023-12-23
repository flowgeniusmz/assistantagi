import streamlit as st

def add_msg_to_msgs(vRole, vContent):
    message = {
        "role": vRole,
        "content": vContent
    }

    if "messages" not in st.session_state:
        st.session_state.messages=[]

    print(st.session_state.messages)
    msgs = st.session_state.messages.append(message)
    print(st.session_state.messages)

    return msgs