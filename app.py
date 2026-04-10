import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Arogya Mitra AI", page_icon="🏥")
st.title("🏥 Arogya Mitra AI")

# --- CSS: Compact Bottom Bar ---
st.markdown("""
    <style>
    .block-container { padding-bottom: 8rem; }
    
    /* Center the bottom bar and keep it small */
    .stChatInputContainer {
        width: 80% !important;
        margin: 0 auto !important;
    }
    
    /* Position the language selector right next to the input */
    .fixed-lang {
        position: fixed;
        bottom: 100px;
        right: 10%;
        width: 100px;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# Language Selector (Floating just above the bar)
st.markdown('<div class="fixed-lang">', unsafe_allow_html=True)
lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Search Bar at the bottom
prompt = st.chat_input("Ask me about health...", accept_audio=True)

if prompt:
    # Display message
    user_label = prompt["text"] if prompt["text"] else "🎤 Audio message"
    with st.chat_message("user"):
        st.write(user_label)
        
    # Get AI Response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            # Add language context to the prompt
            contextual_prompt = prompt.copy()
            if contextual_prompt["text"]:
                contextual_prompt["text"] = f"(Respond in {lang}) " + contextual_prompt["text"]
            
            response = generate_response(contextual_prompt)
            st.write(response)
