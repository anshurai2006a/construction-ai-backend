from pydantic import BaseModel

class TranscriptionResponse(BaseModel):
    text: str

class TTSRequest(BaseModel):
    text: str