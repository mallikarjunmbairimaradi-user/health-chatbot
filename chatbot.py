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
        response = model.generate_content(user_input)
        return response.text if response.text else "No response generated."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# UI (Simplified)
st.title("Health Awareness Chatbot")
user_query = st.text_input("Ask a question:")
if st.button("Send") and user_query:
    st.write(generate_response(user_query))
