import streamlit as st
from chatbot import generate_response

# Page Config
st.set_page_config(page_title="Jan Swasthya AI", page_icon="🏥")

# Sidebar for Language Selection (Visual Guide)
with st.sidebar:
    st.header("🌐 Language / भाषा")
    # This helps set the 'context' but Gemini will auto-detect too
    lang = st.selectbox("Preferred Language", 
                        ["English", "हिंदी (Hindi)", "ಕನ್ನಡ (Kannada)", "मराठी (Marathi)", "తెలుగు (Telugu)"])
    st.info(f"Chatbot is now optimized for {lang}")

st.title("🏥 Jan Swasthya AI")
st.markdown("### Multilingual Health Awareness Assistant")

# --- VOICE INPUT (Direct Multilingual) ---
audio_input = st.audio_input("Record your query in your mother tongue")

if audio_input:
    with st.chat_message("user"):
        st.write("🎤 Audio Message Received")
    
    with st.chat_message("assistant"):
        with st.spinner("Analyzing audio..."):
            response = generate_response(audio_input.getvalue(), is_audio=True)
            st.markdown(response)

# --- TEXT INPUT ---
if prompt := st.chat_input("Type here (e.g., 'बुखार के लक्षण क्या हैं?')"):
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            response = generate_response(prompt, is_audio=False)
            st.markdown(response)
