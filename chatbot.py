import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use correct model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(user_input):
    try:
        response = model.generate_content(user_input)

        if response.text:
            return response.text
        else:
            return "I couldn't understand. Please try again."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
