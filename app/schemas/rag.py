from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DocumentOut(BaseModel):
    id: int
    filename: str
    doc_type: str
    uploaded_at: datetime
    page_count: Optional[int] = None

    class Config:
        from_attributes = True

class RAGQuery(BaseModel):
    question: str
    doc_type: Optional[str] = None

class SourceChunk(BaseModel):
    document_filename: str
    page_number: Optional[int] = None
    excerpt: str

class RAGResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]
    confidence: Optional[float] = None