import streamlit as st
from chatbot import generate_response

# 1. Page Config for a clean professional look
st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥", layout="centered")

# --- 2. THE CSS: To match the modern AI frame ---
st.markdown("""
    <style>
    /* Hide the standard Streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Make the chat area wider and centered */
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 10rem;
    }

    /* Style the fixed bottom area for the search bar */
    .stChatInputContainer {
        padding-bottom: 20px;
        background-color: transparent !important;
    }

    /* Small CSS hack to place the language selector above the input */
    .floating-lang {
        position: fixed;
        bottom: 90px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1000;
        width: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CHAT HISTORY LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# This loop renders the messages in the "Gemini" bubble style
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. THE UI: BOTTOM BAR ---
# We place the language selector in a "floating" container above the bar
with st.container():
    st.markdown('<div class="floating-lang">', unsafe_allow_html=True)
    lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    # st.chat_input is naturally at the bottom and looks just like Gemini's
    prompt = st.chat_input("Ask me about health...", accept_audio=True)

# --- 5. THE LOGIC ---
if prompt:
    # Handle user message
    user_text = prompt.text if prompt.text else "🎤 Audio Message"
    st.session_state.messages.append({"role": "user", "content": user_text})
    
    with st.chat_message("user"):
        st.markdown(user_text)

    # Handle AI Response
    with st.chat_message("assistant"):
        with st.spinner(""): # Empty spinner for clean look
            # IMPORTANT: Ensure your chatbot.py uses the new name 'Arogya Mitra AI'
            response = generate_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
