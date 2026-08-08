from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.models.document import Document
from app.ai.vector_store import add_to_vector_store, search_vector_store
from app.ai.llm_client import generate_answer
from app.schemas.rag import RAGQuery, RAGResponse, SourceChunk
from app.utils.file_utils import save_upload_file

async def ingest_document(file: UploadFile, doc_type: str, db: Session) -> Document:
    file_path = await save_upload_file(file, subfolder="documents")
    collection_id = add_to_vector_store(file_path, doc_type=doc_type)

    doc = Document(
        filename=file.filename,
        file_path=file_path,
        doc_type=doc_type,
        vector_collection_id=collection_id,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def answer_question(query: RAGQuery, db: Session) -> RAGResponse:
    chunks = search_vector_store(query.question, doc_type_filter=query.doc_type)
    answer_text = generate_answer(question=query.question, context_chunks=chunks)

    sources = [
        SourceChunk(
            document_filename=c["filename"],
            page_number=c.get("page"),
            excerpt=c["text"][:200],
        )
        for c in chunks
    ]
    return RAGResponse(answer=answer_text, sources=sources)