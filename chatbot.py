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
            You are a friendly health awareness chatbot.

            Guidelines:
            - Give simple and clear answers
            - Be supportive and helpful
            - Suggest healthy habits
            - If serious issue, suggest consulting a doctor

            User: {user_input}
            """
        )

        return response.text if response.text else "Sorry, I couldn't understand. Can you rephrase?"

    except Exception as e:
        return "⚠️ Error: Unable to generate response. Please try again."
