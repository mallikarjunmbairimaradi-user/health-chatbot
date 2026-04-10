import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 2026 Update: Use the Gemini 3.1 series
        # gemini-1.5-flash was shut down in Jan 2026
        model = genai.GenerativeModel(
            model_name="gemini-3.1-flash-lite-preview", 
            system_instruction=(
                "You are 'Arogya Mitra AI', a professional health assistant. "
                "Respond in the same language the user uses. "
                "Provide helpful medical awareness and always advise a doctor visit."
            )
        )
        return model
    except Exception as e:
        st.error(f"⚠️ API Error: {e}")
        return None

model = initialize_model()

def generate_response(prompt_data):
    if not model: return "Bot offline."
    try:
        # For 3.1 models, we send the prompt directly
        response = model.generate_content(prompt_data)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
