import streamlit as st
from chatbot import generate_response

# 1. Page Config
st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥", layout="wide")

# 2. CSS to handle the layout and prevent "out of frame" issues
st.markdown("""
    <style>
    /* Ensure the main content doesn't get hidden behind the bottom bar */
    .block-container {
        padding-bottom: 10rem;
    }
    
    /* Make the bottom bar clean and fixed */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Styles the container for the search and language bar */
    .bottom-bar {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
        display: flex;
        gap: 10px;
        align-items: center;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CHAT HISTORY (Keep your session_state logic here)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. FIXED BOTTOM BAR (This is the fix)
# Instead of columns inside a container, we use st.chat_input directly 
# and put the language selector in the sidebar or just above it.

# Floating Language Selection just above the chat bar
col_space, col_select = st.columns([0.8, 0.2])
with col_select:
    lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")

# The Chat Input (Streamlit automatically pins this to the bottom correctly)
prompt = st.chat_input("Ask me about health...", accept_audio=True)

# 5. CHAT LOGIC
if prompt:
    # (Your existing logic to handle prompt.text and prompt.audio)
    user_msg = prompt.text if prompt.text else "🎤 Audio Message"
    st.session_state.messages.append({"role": "user", "content": user_msg})
    
    with st.chat_message("user"):
        st.markdown(user_msg)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            # Pass the lang context and the prompt to your chatbot
            response = generate_response(prompt) 
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Force a rerun to show messages instantly
    st.rerun()
