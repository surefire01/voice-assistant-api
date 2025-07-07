
# 🗣️ Voice Assistant Starter Template

A simplified, general-purpose voice assistant backend you can use as a starting point to build your own custom voice-driven applications.

This project lets you **ask questions in voice** and get **AI-generated audio replies**, demonstrating streaming audio processing, speech-to-text, LLM-powered responses, and text-to-speech output.

**Why?**  
I built this as a *minimal* example for developers wanting to create their own voice-based assistants. It abstracts away boilerplate and offers a clear foundation to customize further.

---

## ✨ Features

- Accepts voice input and generates AI audio replies
- Streams audio for low latency
- Modular FastAPI backend
- Easy to extend for your own use case

---

## 🛠️ Quick Setup

> ⚠️ **Requires Python 3.12 only**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### 2️⃣ Verify Python Version

Ensure you're using Python 3.12:

```bash
python --version
# Should output: Python 3.12.x
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

This project requires an API key from [Mistral.ai](https://docs.mistral.ai/getting-started/api-quickstart/).

Create a `.env` file in the root directory:

```
API_KEY=your_mistral_api_key_here
```

You can get your Mistral API key by signing up and following their [API Quickstart Guide](https://docs.mistral.ai/getting-started/api-quickstart/).

---

## ▶️ Running the Project

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access it in your browser or API client at:

```
http://localhost:8000
```

---

## 📣 Example Interaction

1. Open your browser and visit the `/ui` endpoint:

```
http://localhost:8000/ui
```

2. Use the simple web interface to record your question.
3. Get an AI-generated audio reply that you can listen to directly.

---

## 🏗️ Architecture

- Gradio-based Web UI streams audio via WebRTC to FastAPI backend.
- Voice Activity Detection (VAD) logic first detects speech start and stop.
- Detected speech segments are transcribed to text.
- Text is sent to the LLM (Mistral) for generating a response.
- The response text is converted to speech using TTS.
- Audio reply is streamed back to the user in real time.


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
