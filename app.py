import streamlit as st
from chatbot import generate_response

st.title("🩺 Health Awareness Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.write("🧑", msg)
    else:
        st.write("🤖", msg)
        