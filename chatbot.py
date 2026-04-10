import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # UPGRADE: Using the 2026 stable model name
        model = genai.GenerativeModel(
            model_name="gemini-3.1-flash-lite", 
            system_instruction="You are Jan Swasthya AI. Support all Indian languages."
        )
        return model
    except Exception as e:
        st.error(f"Init Error: {e}")
        return None

model = initialize_model()

def generate_response(prompt_data):
    if not model: return "Model offline."
    try:
        # Gemini 3.1 handles the combined dict from st.chat_input automatically
        response = model.generate_content(prompt_data)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
