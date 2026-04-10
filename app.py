import streamlit as st
from chatbot import generate_response

st.title("🏥 Jan Swasthya AI")

# --- UI Layout: Sidebar for clean look ---
with st.sidebar:
    st.header("🌐 Language")
    lang = st.radio("Select Mode", ["English", "Hindi", "Kannada", "Marathi"], index=0)

# --- The "Unified" Bottom Bar ---
# st.chat_input in 2026 now supports 'accept_audio' directly
# This places the Mic INSIDE the bar on the right automatically.
prompt = st.chat_input("Ask me about health...", accept_audio=True)

if prompt:
    # 1. Handle Voice Input
    if prompt.audio:
        with st.chat_message("user"):
            st.write(f"🎤 Audio Message ({lang})")
        with st.chat_message("assistant"):
            with st.spinner("Analyzing audio..."):
                # Pass audio + language context to Gemini
                response = generate_response([
                    {"mime_type": "audio/wav", "data": prompt.audio.getvalue()},
                    f"Please respond in {lang}."
                ])
                st.write(response)
    
    # 2. Handle Text Input
    elif prompt.text:
        with st.chat_message("user"):
            st.write(prompt.text)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(f"Language: {lang}. Query: {prompt.text}")
                st.write(response)
