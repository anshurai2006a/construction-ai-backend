from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
from app.schemas.voice import TranscriptionResponse, TTSRequest
from app.services.voice_service import speech_to_text, text_to_speech

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    text = speech_to_text(audio_bytes)
    return TranscriptionResponse(text=text)

@router.post("/speak")
def speak(payload: TTSRequest):
    audio_bytes = text_to_speech(payload.text)
    return Response(content=audio_bytes, media_type="audio/mpeg")