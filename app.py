import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Jan Swasthya AI", page_icon="🏥")
st.title("🏥 Arogya Mitra AI")

# --- 1. SESSION STATE (Ensures messages are visible) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 2. BOTTOM UI (Search bar + Language) ---
# We use a container to keep this at the bottom
with st.container():
    # Create columns: Large for Search, Small for Language
    col_search, col_lang = st.columns([0.8, 0.2])
    
    with col_lang:
        # Language selector next to search bar
        lang = st.selectbox("🌐", ["EN", "HI", "KN", "MR"], label_visibility="collapsed")
    
    with col_search:
        # Search bar with integrated Mic
        prompt = st.chat_input("Ask me about health...", accept_audio=True)

# --- 3. CHAT LOGIC ---
if prompt:
    # Handle both text and audio
    user_content = prompt.text if prompt.text else "🎤 Voice Message"
    
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_content})
    with st.chat_message("user"):
        st.markdown(user_content)

    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            # Prepare data for Gemini
            if prompt.audio:
                input_data = [
                    {"mime_type": "audio/wav", "data": prompt.audio.getvalue()},
                    f"Please respond in language code: {lang}"
                ]
            else:
                input_data = f"Language {lang}: {prompt.text}"
                
            response = generate_response(input_data)
            st.markdown(response)
            
            # Save assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 4. AUTO-SCROLL ---
# This small piece of CSS ensures the chat stays scrolled to the bottom
st.markdown("<div id='end'></div>", unsafe_allow_html=True)
