# main.py
import re
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastrtc import AlgoOptions,  ReplyOnPause, Stream, get_silero_model, SileroVadOptions, get_stt_model
from fastrtc.utils import CloseStream
import os
import gradio as gr
from dotenv import load_dotenv
from coqui_tts import get_tts_model, CoquiTTSOptions
from mistarlai import MistrialAI

# load environment variables
load_dotenv()

# fastApi app
app = FastAPI()

# Load models
stt_model = get_stt_model()
tts_model = get_tts_model()
vad_model = get_silero_model()
llm_client = MistrialAI(api_key=os.getenv("MISTRALAI"))

def isTextValid(text=str) -> bool:
    if(len(text) <1): return False
    if re.match(r"^\[.*\]$", text):
        return False
    
    return True

# this function handles the audio received from the reply on pause method 
def audioHanlder(audio):
    
    prompt = stt_model.stt(audio)
    prompt = prompt.strip()
    
    if isTextValid(prompt):
        print(f"User: {prompt}")
        
        assistant_reply  = llm_client.chat(prompt)
        print(f"Assistant: {assistant_reply}")
    
        for chunk in tts_model.stream_tts_sync(assistant_reply) :
            yield chunk


def onstart():
    for chunk in tts_model.stream_tts_sync("Hello! how can I help you today?") :
                yield chunk

# audio stream    
stream = Stream(
    ReplyOnPause(
        audioHanlder,
        startup_fn=onstart,
        algo_options=AlgoOptions(
            audio_chunk_duration=0.4,
            started_talking_threshold=0.2,
            speech_threshold=0.1
        ),
        model_options=SileroVadOptions(
                threshold=0.5,                  # slightly stricter to avoid noise triggering speech
                min_speech_duration_ms=100,    # detect short phrases like "yes", "no", "ok"
                max_speech_duration_s=20.0,    # split long speech at 10s
                min_silence_duration_ms=800,   # detect pause faster (~0.6s)
                window_size_samples=1024,      # stable default for 16kHz
                speech_pad_ms=200              # tight pad, low latency (can go lower)
        ),
        model=vad_model
    ),
    modality="audio",
    mode="send-receive",
)
   
# root
@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello, FastAPI is working!"})

app = gr.mount_gradio_app(app, stream.ui, path="/ui")
