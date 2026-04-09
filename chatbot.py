import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use the latest 2026 stable preview model
# Note: Ensure you do NOT use "models/text-bison" or "models/gemini-1.5"
model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-preview",
    system_instruction="You are a professional Health Awareness Chatbot for disease awareness. Be helpful and accurate."
)

def generate_response(user_input):
    try:
        # The current method for Gemini models
        response = model.generate_content(user_input)
        
        if response.text:
            return response.text
        else:
            return "I'm having trouble understanding. Could you rephrase?"

    except Exception as e:
        # This will show you if the API key itself is the issue
        return f"⚠️ API Error: {str(e)}"
