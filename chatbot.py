import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use the Gemini 3.1 Flash model (Current 2026 Stable)
model = genai.GenerativeModel(
    model_name="gemini-3.1-flash",
    system_instruction="You are a Health Awareness Assistant for disease awareness. Provide concise, accurate info and always remind users to consult a professional."
)

def generate_response(user_input):
    try:
        response = model.generate_content(user_input)
        if response.text:
            return response.text
        return "I couldn't process that. Please try again."
    except Exception as e:
        # If this fails, it will print the specific model-related error
        return f"⚠️ Connection Error: {str(e)}"
