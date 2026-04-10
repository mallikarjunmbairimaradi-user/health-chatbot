import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥")

# --- CUSTOM CSS: Unified Bottom Bar ---
st.markdown("""
    <style>
    /* 1. Fix the container to the bottom and center it */
    .bottom-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 70%; /* Adjust this to make the bar smaller/larger */
        max-width: 800px;
        z-index: 1000;
        display: flex;
        align-items: center;
        background-color: #262730; /* Matches dark theme */
        border: 1px solid #464646;
        border-radius: 15px;
        padding: 5px 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* 2. Style the language dropdown to look like it's part of the bar */
    .stSelectbox {
        width: 80px !important;
        margin-right: 10px;
    }
    
    /* 3. Ensure the chat input doesn't have its own bulky container */
    .stChatInput {
        flex-grow: 1;
    }
    
    /* 4. Hide standard Streamlit padding that pushes things out of frame */
    footer {visibility: hidden;}
    .block-container {padding-bottom: 100px;}
    </style>
    """, unsafe_allow_html=True)

# --- CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE UNIFIED BOTTOM BAR ---
# We use an empty placeholder to inject our elements into the flexbox
with st.container():
    # This creates the visual 'bar'
    st.markdown('<div class="bottom-container">', unsafe_allow_html=True)
    
    # We use columns ONLY for the input elements to live inside the flexbox
    c1, c2 = st.columns([0.15, 0.85])
    
    with c1:
        # Language dropdown inside the bar
        lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")
    
    with c2:
        # Search bar with Mic inside the bar
        prompt = st.chat_input("Ask me about health...", accept_audio=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOGIC ---
if prompt:
    user_content = prompt.text if prompt.text else "🎤 Audio Message"
    st.session_state.messages.append({"role": "user", "content": user_content})
    with st.chat_message("user"):
        st.markdown(user_content)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            # Update chatbot.py instructions if it still says the old name!
            response = generate_response(prompt) 
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
