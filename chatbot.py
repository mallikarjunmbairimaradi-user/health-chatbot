import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Using the standard naming convention for 2026
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash", 
            system_instruction=(
                "You are Jan Swasthya AI. Respond in the user's language. "
                "Provide health awareness and always advise seeing a doctor."
            )
        )
        return model
    except Exception as e:
        # If it fails, try the fallback name
        st.warning("Trying fallback model naming...")
        return genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_response(user_input, is_audio=False):
    if not model: return "Bot not configured."
    
    try:
        if is_audio:
            # Gemini hears the audio and identifies the language automatically
            content = [
                {"mime_type": "audio/wav", "data": user_input},
                "Analyze this health query and respond in the speaker's language."
            ]
        else:
            content = user_input

        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
