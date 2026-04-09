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
        # Add the config here to control speed and length
        response = model.generate_content(
            user_input,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=300,  # Limits length to speed up response
                temperature=0.7,        # Keeps responses balanced and focused
            )
        )
        
        if response.text:
            return response.text
        return "I'm sorry, I couldn't generate a response."

    except Exception as e:
        return f"⚠️ API Error: {str(e)}"
# In your UI section:
if st.button("Send") and user_query:
    with st.spinner("Analyzing..."): # This adds a nice loading animation
        response = generate_response(user_query)
        st.write(response)
