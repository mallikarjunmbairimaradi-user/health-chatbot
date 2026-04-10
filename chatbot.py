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
                "You are 'You are Arogya Mitra AI', a professional health assistant. "
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
        # Check if prompt_data is the dictionary from st.chat_input
        if isinstance(prompt_data, dict):
            content_parts = []
            
            # If there is text, add it
            if prompt_data.get("text"):
                content_parts.append(prompt_data["text"])
                
            # If there is audio, add it as a blob
            if prompt_data.get("audio"):
                content_parts.append({
                    "mime_type": "audio/wav", 
                    "data": prompt_data["audio"].getvalue()
                })
            
            # Send the combined parts to Gemini
            response = model.generate_content(content_parts)
        else:
            # Fallback for simple string input
            response = model.generate_content(prompt_data)
            
        return response.text
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
