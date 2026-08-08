from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.schemas.rag import RAGQuery, RAGResponse, DocumentOut
from app.services.rag_service import ingest_document, answer_question
from app.api.deps import get_db

router = APIRouter()

@router.post("/upload", response_model=DocumentOut)
async def upload_document(
    file: UploadFile = File(...),
    doc_type: str = Form("sop"),
    db: Session = Depends(get_db),
):
    return await ingest_document(file, doc_type, db)

@router.post("/ask", response_model=RAGResponse)
def ask(query: RAGQuery, db: Session = Depends(get_db)):
    return answer_question(query, db)