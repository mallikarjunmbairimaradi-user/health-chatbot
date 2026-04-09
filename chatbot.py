import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(user_input):
    try:
        response = model.generate_content(
            f"""
            You are a helpful health awareness assistant.
            Give simple, clear and supportive answers.

            User: {user_input}
            """
        )
        return response.text if response.text else "Please rephrase your question."
    except Exception:
        return "⚠️ Error generating response. Try again."
