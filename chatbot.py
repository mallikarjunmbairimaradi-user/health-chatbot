import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
def initialize_model():
    try:
        # Using Streamlit Secrets for 2026 industry standards
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # System instructions ensure the bot stays in "Health Mode"
        model = genai.GenerativeModel(
            model_name="gemini-3.1-flash-lite-preview",
            system_instruction=(
                "You are an empathetic Public Health Awareness Chatbot named Jan Swasthya AI. "
                "Provide accurate, simple information about diseases and vaccines. "
                "Support multiple languages. Always end with a disclaimer to consult a doctor."
            )
        )
        return model
    except Exception as e:
        st.error("⚠️ Configuration Error: Ensure GEMINI_API_KEY is in .streamlit/secrets.toml")
        return None

# Initialize model globally
model = initialize_model()

# --- 2. THE CHAT LOGIC ---
def generate_response(user_input):
    if not model:
        return "Chatbot is not configured."
        
    try:
        # Optimized config for sub-second responses
        response = model.generate_content(
            user_input,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=350,
                temperature=0.7,
            )
        )
        
        if response.text:
            return response.text
        return "I'm sorry, I couldn't generate a response."

    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
