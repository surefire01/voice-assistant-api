import asyncio
import re
from functools import lru_cache
from dataclasses import dataclass
from typing import Optional, AsyncGenerator, Generator
import click
import numpy as np
from numpy.typing import NDArray

from TTS.api import TTS  # coqui-tts >= 0.26.2
from fastrtc.text_to_speech.tts import TTSModel


@dataclass
class CoquiTTSOptions:
    speaker: Optional[str] = None               # Speaker ID (multi-speaker models)
    speaker_wav: Optional[str] = None           # Path to WAV for cloning
    lang: Optional[str] = None                  # Language ID (for multilingual models)


@lru_cache
def get_tts_model() -> TTSModel:
    model = CoquiTTSModel()
    print(click.style("INFO", fg="green") + ":\t  Warming up TTS model.")
    
    model.tts("Hello, world!", options=CoquiTTSOptions(speaker="p225"))  # Warm-up
    print(click.style("INFO", fg="green") + ":\t  TTS model warmed up.")
    return model

class CoquiTTSModel(TTSModel):
    def __init__(self, model_name: str = "tts_models/en/vctk/vits"):
        print(f"Initializing Coqui TTS model... {model_name}")

        self.device = "cuda" if self._has_cuda() else "cpu"
        self.model = TTS(model_name).to(self.device)

        self.sampling_rate = self.model.synthesizer.output_sample_rate

    def _has_cuda(self) -> bool:
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False

    def tts(
        self, text: str, options: Optional[CoquiTTSOptions] = None
    ) -> tuple[int, NDArray[np.float32]]:
        options = options or CoquiTTSOptions()

        audio = self.model.tts(
            text,
            speaker=options.speaker,
            speaker_wav=options.speaker_wav,
            language=options.lang
        )
        return self.sampling_rate, np.array(audio, dtype=np.float32)

   
    async def stream_tts(self, text: str, options: Optional[CoquiTTSOptions] = None
                        ) -> AsyncGenerator[tuple[int, NDArray[np.float32]], None]:
        options = options or CoquiTTSOptions()
        # Split into sentences—preserves punctuation
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        chunk_size = 2048  # tweakable for latency/size balance

        for sentence in sentences:
            if not sentence:
                continue
            wav = self.model.tts(sentence,
                                 speaker=options.speaker,
                                 speaker_wav=options.speaker_wav,
                                 language=options.lang)
            arr = np.array(wav, dtype=np.float32)

            # Yield audio in manageable chunks, skipping only true silence
            for i in range(0, len(arr), chunk_size):
                chunk = arr[i:i + chunk_size]
                # Only skip if the chunk is truly silent (all values very close to zero)
                if np.max(np.abs(chunk)) < 1e-4:
                    continue
                yield self.sampling_rate, chunk

    def stream_tts_sync(
        self, text: str, options: Optional[CoquiTTSOptions] = None
    ) -> Generator[tuple[int, NDArray[np.float32]], None, None]:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        iterator = self.stream_tts(text, options).__aiter__()
        while True:
            try:
                yield loop.run_until_complete(iterator.__anext__())
            except StopIteration:
                break
            except StopAsyncIteration:
                break
