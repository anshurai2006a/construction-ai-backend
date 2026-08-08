from app.ai.stt import transcribe_audio
from app.ai.tts import synthesize_speech

def speech_to_text(audio_bytes: bytes) -> str:
    return transcribe_audio(audio_bytes)

def text_to_speech(text: str) -> bytes:
    return synthesize_speech(text)