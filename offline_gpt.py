import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"\n🤖 Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening... (you have 10 seconds)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            user_input = recognizer.recognize_google(audio)
            print(f"🧑 You: {user_input}")
            return user_input.lower()
        except sr.WaitTimeoutError:
            return "timeout"
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech service error."

def reply_to(text):
    if "hello" in text:
        return "Hello! How can I help you today?"
    elif "your name" in text:
        return "I'm a free offline chatbot built with Python."
    elif "bye" in text or "exit" in text:
        return "Goodbye! Have a great day."
    elif "how are you" in text:
        return "I'm just code, but I'm doing fine!"
    else:
        return "I don't understand that, but I'm learning!"

# Main loop
if __name__ == "__main__":
    speak("Hi! I'm your offline voice chatbot.")
    while True:
        text = listen()
        if text == "timeout":
            speak("You didn't say anything. Try again.")
            continue
        response = reply_to(text)
        speak(response)
        if "bye" in text or "exit" in text:
            break
