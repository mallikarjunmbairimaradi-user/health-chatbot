import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 Refined Instruction for better English/Multilingual balance
        model = genai.GenerativeModel(
            model_name="gemini-3.1-flash-lite-preview", # Using the most stable multimodal version
            system_instruction=(
                "You are 'Arogya Mitra AI', a professional health assistant. "
                "1. If the user speaks or types in English, respond in English. "
                "2. If the user uses a regional language (Hindi, Kannada, etc.), respond in that same language. "
                "3. Use simple, clear terms for health awareness. "
                "4. Always include a disclaimer to consult a doctor."
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
        # We wrap the prompt_data to ensure the model focuses on language detection
        response = model.generate_content(
            prompt_data,
            generation_config=genai.types.GenerationConfig(
                temperature=0.4, # Lower temperature makes language detection more stable
            )
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
