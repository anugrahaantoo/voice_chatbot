import openai
import speech_recognition as sr
import pyttsx3
import os

from dotenv import load_dotenv
load_dotenv()

# Your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize recognizer and TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"\n🤖 GPT: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=8)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"🧑 You: {user_input}")
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, there's a network issue."

def get_gpt_response(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm your voice chatbot powered by GPT.")
    while True:
        user_text = listen()
        if "bye" in user_text.lower():
            speak("Goodbye! Talk to you soon.")
            break
        gpt_reply = get_gpt_response(user_text)
        speak(gpt_reply)
