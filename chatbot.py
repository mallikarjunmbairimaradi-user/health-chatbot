import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the model with a System Instruction for your health chatbot
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a helpful and empathetic Health Awareness Chatbot. "
                       "Provide accurate information about diseases and wellness. "
                       "Always include a disclaimer that you are an AI and users "
                       "should consult a doctor for medical advice."
)

def generate_response(user_input):
    try:
        # Use the updated model method
        response = model.generate_content(user_input)
        
        if response.text:
            return response.text
        else:
            return "I'm sorry, I couldn't generate a response. Could you rephrase that?"

    except Exception as e:
        # Catching specific errors like invalid API keys or quota limits
        return f"⚠️ API Error: {str(e)}"
