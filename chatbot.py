import google.generativeai as genai
import streamlit as st

# --- 1. INITIALIZATION ---
def initialize_model():
    try:
        # Get key from secrets
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # We use 'gemini-1.5-flash' - it is the most stable name
        # If 'models/' prefix caused an error, this version is cleaner
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", 
            system_instruction=(
                "You are 'Jan Swasthya AI', a multilingual health assistant. "
                "Detect the user's language and respond in that same language. "
                "Always advise users to consult a doctor."
            )
        )
        return model
    except Exception as e:
        # If initialization fails, we print the error to Streamlit so you can see it
        st.error(f"Initialization Failed: {e}")
        return None

# CRITICAL: Define the model variable globally
model = initialize_model()

# --- 2. RESPONSE LOGIC ---
def generate_response(user_input, is_audio=False):
    # Use global to ensure we are talking to the model defined above
    global model
    
    if model is None:
        return "⚠️ Bot is not configured. Please check your API Key in secrets.toml."
    
    try:
        if is_audio:
            content = [
                {"mime_type": "audio/wav", "data": user_input},
                "Analyze this health query and respond in the speaker's mother tongue."
            ]
        else:
            content = user_input

        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
