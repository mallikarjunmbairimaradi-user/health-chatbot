import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 LOGIC FIX: Try the 2026 stable identifier first
        # gemini-1.5-flash and gemini-3.1-flash often cause 404s if 
        # the 'models/' prefix is missing or if the API version is mismatched.
        
        model_name = "gemini-1.5-flash" # Use the base name for maximum compatibility
        
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=(
                "You are Arogya Mitra AI. Detect the language of the input "
                "and respond in that same language. Stay professional and health-focused."
            )
        )
        return model
    except Exception as e:
        # If the first attempt fails, we don't crash the app
        return None

# Global model instance
model = initialize_model()

def generate_response(input_parts):
    global model
    # If the model failed to initialize at start, try a last-resort fallback here
    if model is None:
        try:
            fallback_name = "gemini-pro" # The most reliable fallback in Google's history
            model = genai.GenerativeModel(fallback_name)
        except:
            return "⚠️ API Connection Error. Please verify your API Key in secrets."

    try:
        # Multimodal generation
        response = model.generate_content(input_parts)
        if response and response.text:
            return response.text
        return "I'm sorry, I couldn't generate a text response. Please try again."
    except Exception as e:
        # This catches the 404 specifically during the call
        return f"⚠️ API Error: {str(e)}. Tip: Ensure your API key has access to the Gemini API."
