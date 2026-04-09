import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Correct working model for this SDK
model = genai.GenerativeModel("models/text-bison-001")


def generate_response(user_input):
    try:
        response = model.generate_content(user_input)

        if response.text:
            return response.text
        else:
            return "I couldn't understand. Please try again."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
