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
                "You are 'Arogya Mitra AI', an empathetic health assistant. "
                "CRITICAL LANGUAGE RULE: "
                "1. If the user types in English, respond in English. "
                "2. If the user types in a regional language using ROMAN script (English alphabets), "
                "   e.g., 'namaskara' (Kannada) or 'kaise ho' (Hindi), you MUST detect the language "
                "   and respond back using ROMAN script in that same language. "
                "3. If they use native script (ಕನ್ನಡ, हिंदी), respond in native script. "
                "4. Always provide simple health advice and include a medical disclaimer."
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
