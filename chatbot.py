import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 2026 Fix: Using the highly compatible 'flash-8b' string
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-8b", 
            system_instruction=(
                "You are 'Arogya Mitra AI'. Always detect the language "
                "of the user and respond in that same language. "
                "Provide simple health info and always include a medical disclaimer."
            )
        )
        return model
    except Exception as e:
        st.error(f"⚠️ Init Error: {e}")
        return None

model = initialize_model()

def generate_response(input_parts):
    if not model: return "Bot not configured."
    try:
        # Pass text/audio list directly
        response = model.generate_content(input_parts)
        return response.text if response.text else "I couldn't process that request."
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
