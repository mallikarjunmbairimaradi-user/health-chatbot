import streamlit as st
from chatbot import generate_response
from openai import OpenAI  # Used for the Whisper model
import io

# Initialize the OpenAI client for transcription
# (Make sure OPENAI_API_KEY is also in your secrets.toml)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🏥 Jan Swasthya AI")

# --- VOICE INPUT SECTION ---
audio_data = st.audio_input("Record your health query")

if audio_data:
    with st.spinner("Converting speech to text..."):
        # 1. Convert the audio bytes into a file-like object
        audio_file = io.BytesIO(audio_data.getvalue())
        audio_file.name = "audio.wav"

        # 2. Use Whisper to transcribe (Supports Hindi, Kannada, etc.)
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        user_query = transcript.text
        st.info(f"You said: {user_query}")

        # 3. Send the transcribed text to your Gemini bot
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                response = generate_response(user_query)
                st.write(response)
