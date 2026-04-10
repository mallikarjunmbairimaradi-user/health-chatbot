import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 2026 LOGIC: Try the latest stable Gemini 2.5 Flash
        # If gemini-2.5-flash is not available, it tries gemini-1.5-flash-latest
        try:
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash", 
                system_instruction="You are Arogya Mitra AI. Support multilingual health queries."
            )
            # Simple check to see if model is reachable
            model.generate_content("test") 
        except:
            # Fallback for older API keys or specific regional restrictions
            model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
            
        return model
    except Exception as e:
        # We return None so the app.py can show a friendly warning
        return None

model = initialize_model()

def generate_response(input_parts):
    if not model:
        return "⚠️ Bot connection failed. Please check your internet or API key."
    try:
        response = model.generate_content(input_parts)
        return response.text if response.text else "I couldn't generate a response."
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
