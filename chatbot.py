import streamlit as st
from openai import OpenAI

# connect API using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful health awareness assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
