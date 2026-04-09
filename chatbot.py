import streamlit as st
import google.generativeai as genai
import time

# --- 1. CONFIGURATION ---
# Access your API Key from Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Missing API Key. Please check your streamlit secrets.")

# Use Gemini 3.1 Flash-Lite for maximum speed and sub-second feedback
# This model is the current 2026 standard for high-speed chat
model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite-preview",
    system_instruction=(
        "You are an empathetic Public Health Awareness Chatbot. "
        "Provide accurate information about diseases, prevention, and wellness. "
        "Keep responses concise and always advise users to consult a doctor."
    )
)

# --- 2. THE CHAT LOGIC ---
def generate_response(user_input):
    try:
        # stream=True provides the "instant" typing effect
        response = model.generate_content(
            user_input,
            stream=True,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=300,
                temperature=0.7,
            )
        )
        return response

    except Exception as e:
        # Handling the "429 Quota Exceeded" error gracefully
        if "429" in str(e):
            st.warning("⏱️ Rate limit reached. Waiting 30 seconds before next request...")
            time.sleep(5) # Brief pause
            return None
        else:
            st.error(f"⚠️ API Error: {str(e)}")
            return None

# --- 3. STREAMLIT UI ---
# --- In your UI section ---
if st.button("Send") and user_query:
    response_stream = generate_response(user_query)
    
    if response_stream:
        # st.write_stream is the magic part that fixed the JSON/Object view
        st.write_stream(response_stream)
