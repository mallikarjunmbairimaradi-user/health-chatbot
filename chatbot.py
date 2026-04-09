import streamlit as st
import google.generativeai as genai

# Configure
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 1. DEBUG STEP: This will print the models you actually have access to in your terminal
# This helps if 'gemini-3-flash-preview' is also blocked for some reason
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Available Model: {m.name}")
except:
    pass

# 2. THE FIX: Use the explicit v1beta path
model = genai.GenerativeModel(
    model_name="models/gemini-3-flash-preview",
    system_instruction="You are a Public Health Chatbot. Give disease awareness info."
)

def generate_response(user_input):
    try:
        # Use stream=True for instant word-by-word delivery
        response = model.generate_content(
            user_input,
            stream=True, 
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=200, # Smaller limit = faster start
                temperature=0.6,       # Lower temperature is slightly faster
            )
        )
        return response
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        return None

# --- In your UI section ---
if st.button("Send") and user_query:
    # This is the magic part for sub-second UI feedback
    response_stream = generate_response(user_query)
    if response_stream:
        st.write_stream(response_stream)
