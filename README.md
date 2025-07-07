
# 🗣️ Voice Assistant Starter Template

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
<!-- ![Stars](https://img.shields.io/github/stars/surefire01/voice-assistant-api?style=social) -->

A simplified, general-purpose voice assistant backend you can use as a starting point to build your own custom voice-driven applications.

This project lets you **ask questions in voice** and get **AI-generated audio replies**, demonstrating streaming audio processing, speech-to-text, LLM-powered responses, and text-to-speech output.

## 🎥 Demo
https://github.com/user-attachments/assets/e0f5de26-a5b6-4b7a-b29f-060ba0a7f029




---

## ✨ Features

- Accepts voice input and generates AI audio replies
- Streams audio for low latency
- Modular FastAPI backend
- Easy to extend for your own use case

---

## 🎯 Use Cases

- Personal voice assistants
- Customer support bots
- Interactive voice apps
- Smart home interfaces

---

## 🛠️ Quick Setup

> ⚠️ **Requires Python 3.11 only**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### 2️⃣ Verify Python Version

Make sure you're using Python 3.11:

```bash
python --version
# Should output: Python 3.11.x
```

If not, install it from [python.org](https://www.python.org/downloads/).

---

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

---

### 4️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5️⃣ Install ffmpeg

This project needs ffmpeg for audio processing:

* **macOS**

  ```bash
  brew install ffmpeg
  ```

* **Ubuntu/Linux**

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

* **Windows**

  Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your PATH.

---

### 6️⃣ Create Environment File

Get your Mistral API key by signing up and following their [API Quickstart Guide](https://docs.mistral.ai/getting-started/api-quickstart/).

Create a `.env` file:

```
API_KEY=your_mistral_api_key_here
```

---

Sure—here’s a **clean snippet** you can drop right into your README under the **Setup** section (e.g., after **Install ffmpeg**) or as a new **Install eSpeak** step:

---

### 7️⃣ Install eSpeak

This project uses eSpeak to enable additional Coqui TTS voice models.

**💻 Windows**

1. Download and install eSpeak for Windows:
   👉 [https://espeak.sourceforge.net/](https://espeak.sourceforge.net/)
2. After installation, add the `espeak/command-line` folder to your **PATH** environment variable so the `espeak` command is available in the terminal.

---

**🐧 Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install espeak
```

---

**🍎 macOS**

```bash
brew install espeak
```

---


## ▶️ Running the Project

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Access it in your browser or API client at:

```
http://localhost:8000
```

---

## 📣 Example Interaction

1. Visit the `/ui` endpoint in your browser:

```
http://localhost:8000/ui
```

2. Use the web interface to record your question.
3. Hear an AI-generated audio reply instantly.

---

## 🏗️ Architecture

* Gradio web UI streams audio to the FastAPI backend.
* Voice Activity Detection (VAD) finds when speech starts and stops.
* Detected speech is transcribed to text.
* Text is sent to the LLM (Mistral) to generate a response.
* The response is converted to speech with TTS.
* Audio reply streams back to the user in real time.

---

## 🧩 Next Steps

* Swap in your preferred LLM
* Customize prompts or dialogue logic
* Add authentication and logging
* Containerize with Docker
* Deploy on AWS Lambda, ECS, etc.

---

## 🙏 Credits

Built to help anyone bootstrap their own voice assistant with clean, minimal code.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📫 Questions?

Open an issue or reach out on [LinkedIn](https://www.linkedin.com/in/harshal-awaghad).


