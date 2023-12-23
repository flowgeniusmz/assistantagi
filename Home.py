import streamlit as st
import Testing.display as d
import Testing.assistant as a

# Initialize messages array
if "messages" not in st.session_state:
    st.session_state.messages = []
    initial_assistant_message = "Welcome to FlowGeniusAI! How may I help you?"
    msgs = d.add_msg_to_msgs("assistant", initial_assistant_message)

st.title("Example AI Chat")
st.divider()

messages = st.session_state.messages

for msg in messages:
    role = msg['role']
    content = msg['content']
    chat_msg = st.chat_message(role).markdown(content)

if prompt := st.chat_input():
    d.add_msg_to_msgs("user", prompt)
    st.chat_message("user").markdown(prompt)
    selectedthread = a.thread_selector(prompt)
    selectedthread_messages = a.get_selected_thread_messages(selectedthread)
    selectedthread_display = a.get_response_from_message_list(selectedthread_messages)
    d.add_msg_to_msgs("assistant", selectedthread_display)
    st.chat_message("assistant").markdown(selectedthread_display)