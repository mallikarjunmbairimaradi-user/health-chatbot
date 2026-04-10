import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # SYSTEM INSTRUCTION: This is the key for Auto-Detection
       # Use the most stable naming convention
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest", 
    system_instruction=(
        "You are 'Arogya Mitra AI'. Detect the user's language automatically "
        "and respond in the same language. Always advise consulting a doctor."
    )
)
        return model
    except Exception as e:
        st.error(f"Init Error: {e}")
        return None

model = initialize_model()

def generate_response(input_parts):
    if not model: return "Bot offline."
    try:
        # Pass the text/audio list directly; Gemini handles detection natively
        response = model.generate_content(input_parts)
        return response.text if response.text else "I couldn't process that."
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
