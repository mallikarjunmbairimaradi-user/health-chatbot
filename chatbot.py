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
        # Add the config here to control speed and length
        response = model.generate_content(
            user_input,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=300,  # Limits length to speed up response
                temperature=0.7,        # Keeps responses balanced and focused
            )
        )
        
        if response.text:
            return response.text
        return "I'm sorry, I couldn't generate a response."

    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# --- 3. STREAMLIT UI ---
# --- In your UI section ---
if st.button("Send") and user_query:
    with st.spinner("Analyzing..."): # This adds a nice loading animation
        response = generate_response(user_query)
        st.write(response)
