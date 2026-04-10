import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 Fix: Use the standard stable name without the 'models/' prefix
        # This is the most compatible version for Streamlit Cloud
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", 
            system_instruction=(
                "You are 'Arogya Mitra AI', a helpful health assistant. "
                "Detect the user's language and respond in that same language. "
                "Keep answers simple and always include a medical disclaimer."
            )
        )
        return model
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")
        return None

model = initialize_model()

def generate_response(input_parts):
    if not model: return "Bot is currently offline."
    try:
        # Pass the text/audio list to Gemini
        response = model.generate_content(input_parts)
        return response.text if response.text else "I'm sorry, I couldn't process that."
    except Exception as e:
        # If 1.5-flash fails, try one more fallback
        return f"⚠️ API Error: {str(e)}"
