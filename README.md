Here is your complete `README.md` content, fully formatted and ready to copy into your project:

---


# 🗣️ Voice Chatbot using GPT (Terminal + Web)

This project enables **voice-based interaction with a chatbot powered by OpenAI's GPT API**. You can run it either in the **terminal** or via a **Flask web interface**. It uses `speech_recognition` to capture voice input and `pyttsx3` or `gTTS` for speech output.

---

## ✅ Features

- 🎤 Voice input via microphone (real-time)
- 🤖 GPT-powered intelligent responses
- 🧏 Speech output with text-to-speech
- 💻 Terminal-based interface
- 🌐 Web-based interface (Flask)
- 📡 Offline fallback option (no API)

---

## 📁 Project Structure

```text
voice_chatbot/
├── chatbot.py          # Terminal version
├── web_chatbot.py      # Flask web version
├── offline_gpt.py      # Offline fallback logic
├── templates/
│   └── index.html      # Web UI template
├── requirements.txt    # All Python dependencies
├── .gitignore          # Excludes .env, __pycache__, etc.
└── README.md           # You're reading this!
````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anugrahaantoo/voice_chatbot.git
cd voice_chatbot
```

### 2. Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Set up your OpenAI API Key

1. Visit: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Create a new key
3. Create a `.env` file and add:

```env
OPENAI_API_KEY=sk-xxxxxx...
```

> 🔐 Never expose your API key in code. Use `.env` to keep it secure.

---

## 🚀 How to Run

### Terminal Version

```bash
python chatbot.py
```

Say something into your microphone — the chatbot listens and replies with speech.

---

### Web Version

```bash
python web_chatbot.py
```

Then go to: `http://127.0.0.1:5000`

* Click **Start Talking**
* Speak your message
* GPT replies and voice plays
* Past messages are shown below

> ✅ Allow microphone access in your browser.

---

## 📴 Offline Mode (No API Key)

Use fallback mode if no OpenAI access:

```bash
python offline_gpt.py
```

Returns generic responses like:

> You said: “Hello”
> Bot: Hello there!

---

## 🌐 Why Web Version May Not Work Online

* Microphone access is blocked in non-HTTPS public sites
* API keys can’t be safely exposed in frontend
* GitHub Pages is static and doesn’t support Python

✅ Best used **locally** for full features.

---

## 📦 requirements.txt

```
Flask
openai
python-dotenv
SpeechRecognition
PyAudio
pyttsx3
gTTS
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🚫 GitHub Push Issues with API Keys

If you accidentally pushed a secret:

```bash
git reset --soft HEAD~1
# remove secret from code
git add .
git commit -m "Removed API key"
git push --force
```

You can also allow push temporarily at the link GitHub provides (not recommended).

---

## 🙋‍♀️ Credits

Made by **Anugraha Antoo Kanjookaran**
GitHub: [anugrahaantoo](https://github.com/anugrahaantoo)

---

🎙️ Happy talking to your chatbot! 🤖

```

---

Let me know if you’d like the `requirements.txt` shown here as well.
```
