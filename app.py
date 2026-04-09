import streamlit as st
from chatbot import generate_response

st.title("🩺 Health Awareness Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask your health question...")
if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
        
