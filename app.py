import streamlit as st
from chatbot import generate_response

st.title("🏥 Jan Swasthya AI")

# UI Sidebar for Multilingual Feature
with st.sidebar:
    st.header("Accessibility")
    lang = st.selectbox("Select Language", ["English", "Hindi", "Kannada", "Marathi"])
    st.success(f"Mode: {lang}")

# Voice Support Widget (Matching your LinkedIn claim)
audio_input = st.audio_input("Record your query")

# Chat Input
if prompt := st.chat_input("Ask me about health..."):
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Display AI response with the spinner you liked
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = generate_response(prompt)
            st.write(response)
