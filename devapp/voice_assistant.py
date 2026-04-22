import os
import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import numpy as np


# Load env
load_dotenv()

# ✅ Correct OpenAI setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ AI response
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ✅ Voice input (no PyAudio)
def get_voice_input():
    fs = 44100
    seconds = 5

    st.write("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    write("input.wav", fs, np.array(recording))

    recognizer = sr.Recognizer()
    with sr.AudioFile("input.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write(f"You said: {text}")
        return text
    except:
        st.write("Could not understand audio")
        return None

# ✅ Voice output (no gTTS, no playsound)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ✅ Main app
def main():
    st.title("🎤 AI Voice Assistant")

    if st.button("Speak Your Command"):
        user_input = get_voice_input()
        if user_input:
            response = generate_response(user_input)
            st.write(f"Assistant: {response}")
            speak(response)

if __name__ == "__main__":
    main()