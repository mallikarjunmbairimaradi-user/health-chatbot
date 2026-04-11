import google.generativeai as genai
import streamlit as st

def initialize_model():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 🚀 Logic Update: Explicitly handling Transliteration (Hinglish/Kanglish)
        model = genai.GenerativeModel(
            model_name="gemini-3.1-flash-lite-preview", 
            system_instruction=(
                "You are 'Arogya Mitra AI', a helpful health assistant. "
                "STRICT SCRIPT RULES: "
                "1. If the user types in English (e.g., 'Hello'), respond in English. "
                "2. If the user types in Kannada using English letters (e.g., 'Namaskara', 'Nange tale novu ide'), "
                "   you MUST detect that it is Kannada and respond ONLY in KANNADA SCRIPT (ಕನ್ನಡ ಲಿಪಿ). "
                "   Example: User types 'Namaskara', you reply 'ನಮಸ್ಕಾರ! ನಾನು ಆರೋಗ್ಯ ಮಿತ್ರ...' "
                "3. Do NOT use English letters to reply if the user's intent is Kannada. "
                "4. Maintain a professional tone and always include a medical disclaimer in the same language."
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
        # Lowering temperature helps the model stick to the language detection rules
        response = model.generate_content(
            prompt_data,
            generation_config=genai.types.GenerationConfig(
                temperature=0.3, # More focused response
                top_p=0.8,
            )
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
