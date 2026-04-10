import streamlit as st
from chatbot import generate_response

st.title("🏥 Jan Swasthya AI")

# --- CUSTOM CSS FOR ICON POSITIONING ---
st.markdown("""
    <style>
    /* This targets the container holding the chat input and audio */
    .stChatInputContainer {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Optional: Style the audio input to be smaller/compact */
    section[data-testid="stAudioInput"] {
        width: 60px !important;
        min-width: 60px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE UI LAYOUT ---
# Create two columns: one for the search bar (large) and one for the mic (small)
col1, col2 = st.columns([0.85, 0.15])

with col2:
    # This puts the Mic in the "right corner" area
    audio_input = st.audio_input(" ", label_visibility="collapsed")

with col1:
    # Standard Chat Input
    prompt = st.chat_input("Ask me about health...")

# --- LOGIC HANDLING ---

# 1. Handle Voice Input
if audio_input:
    with st.chat_message("user"):
        st.write("🎤 Audio Message Received")
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = generate_response(audio_input.getvalue(), is_audio=True)
            st.markdown(response)

# 2. Handle Text Input
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = generate_response(prompt, is_audio=False)
            st.markdown(response)
