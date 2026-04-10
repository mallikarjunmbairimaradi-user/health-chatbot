import streamlit as st
from chatbot import generate_response

# 1. Page Setup
st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥")
st.title("🏥 Arogya Mitra AI")

# --- CUSTOM CSS: Fixing elements to bottom ---
st.markdown("""
    <style>
    /* This creates a fixed 'dock' at the bottom */
    [data-testid="stVerticalBlock"] > div:has(div.fixed-bottom) {
        position: fixed;
        bottom: 2.5rem;
        background-color: transparent;
        z-index: 999;
        width: 100%;
    }
    
    /* Removes extra padding from the main chat area so it doesn't hide behind the bar */
    .main .block-container {
        padding-bottom: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CHAT HISTORY DISPLAY
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. THE FIXED BOTTOM BAR
# We wrap this in a div with the 'fixed-bottom' class for the CSS to target
with st.container():
    st.markdown('<div class="fixed-bottom">', unsafe_allow_html=True)
    
    # Create columns: Left for Search (85%), Right for Language (15%)
    col_input, col_lang = st.columns([0.85, 0.15])
    
    with col_lang:
        # Language dropdown sitting next to search bar
        lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")
    
    with col_input:
        # Search bar with integrated Mic
        prompt = st.chat_input("Ask me about health...", accept_audio=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# 4. CHAT LOGIC
if prompt:
    user_msg = prompt.text if prompt.text else "🎤 Audio Message"
    
    # Add to history and display
    st.session_state.messages.append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.markdown(user_msg)

    # Response Logic
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            # Pass data to your chatbot logic
            input_context = [prompt.audio.getvalue(), f"Lang: {lang}"] if prompt.audio else f"Lang: {lang}: {prompt.text}"
            response = generate_response(input_context)
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
