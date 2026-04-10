import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥")
st.title("🏥 Arogya Mitra AI")

# --- CSS: Clean Bottom Search Bar ---
st.markdown("""
    <style>
    .block-container { padding-bottom: 8rem; }
    
    /* Center and style the search bar to look professional */
    .stChatInputContainer {
        width: 80% !important;
        margin: 0 auto !important;
        border-radius: 20px;
    }

    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE UNIFIED SEARCH BAR (Bottom Pinned) ---
# Integrated Voice + Text. No separate language bar.
prompt = st.chat_input("Ask me about health...", accept_audio=True)

if prompt:
    # Handle Label for History
    user_label = prompt["text"] if prompt["text"] else "🎤 Audio message"
    st.session_state.messages.append({"role": "user", "content": user_label})
    
    with st.chat_message("user"):
        st.markdown(user_label)

    # AI Response Logic
    with st.chat_message("assistant"):
        with st.spinner("Analyzing Mother Tongue..."):
            # Create the input parts for Gemini
            parts = []
            if prompt["text"]: parts.append(prompt["text"])
            if prompt["audio"]:
                parts.append({
                    "mime_type": "audio/wav", 
                    "data": prompt["audio"].getvalue()
                })
            
            # The bot detects the language from 'parts'
            response = generate_response(parts)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
