import streamlit as st
from chatbot import generate_response

st.title("🏥 Jan Swasthya AI")

# --- CUSTOM CSS: Floating Language Selector ---
st.markdown("""
    <style>
    /* Positions the language selector just above the chat input at the bottom */
    .stSelectbox {
        position: fixed;
        bottom: 85px;
        right: 20px;
        width: 150px !important;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Language selector that "floats" above the input
lang = st.selectbox("Language", ["English", "हिंदी", "ಕನ್ನಡ", "मराठी"], label_visibility="collapsed")

# 2. Unified Chat Input (Voice + Text combined)
# This keeps the bar at the bottom and puts the mic INSIDE the bar
prompt = st.chat_input("Ask me about health...", accept_audio=True)

if prompt:
    # Handle Text Input
    if prompt.text:
        with st.chat_message("user"):
            st.write(prompt.text)
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                response = generate_response(prompt.text)
                st.write(response)
                
    # Handle Audio Input (Inside the same bar)
    if prompt.audio:
        with st.chat_message("user"):
            st.write("🎤 Audio Message Sent")
        with st.chat_message("assistant"):
            with st.spinner("Listening..."):
                # Pass audio data directly to Gemini
                response = generate_response([
                    {"mime_type": "audio/wav", "data": prompt.audio.getvalue()},
                    f"Respond in {lang}"
                ])
                st.write(response)
