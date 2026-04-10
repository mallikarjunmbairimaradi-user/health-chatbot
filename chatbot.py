import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # System instructions optimized for Regional Indian Languages
        model = genai.GenerativeModel(
           model_name="models/gemini-1.5-flash", 
            system_instruction=(
                "You are 'Jan Swasthya AI', a multilingual public health assistant. "
                "Detect the language used by the user (English, Hindi, Kannada, Marathi, etc.) "
                "and respond accurately and empathetically in that SAME language. "
                "Keep medical terms simple so rural users can understand. "
                "Always include a disclaimer in the detected language to consult a doctor."
            )
        )
        return model
    except Exception as e:
        st.error("⚠️ API Configuration Error.")
        return None

model = initialize_model()

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
