from flask import Flask, render_template, request, jsonify
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

# Simple logic
def get_bot_response(message):
    msg = message.lower()
    if "hello" in msg:
        return "Hi there! How can I assist you?"
    elif "your name" in msg:
        return "I am your voice chatbot running on the web."
    elif "bye" in msg:
        return "Goodbye! Take care."
    else:
        return "I didn't understand that, but I'm still learning."

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_reply = get_bot_response(user_msg)
    speak(bot_reply)  # Speak reply in Python (locally)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
