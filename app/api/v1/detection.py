from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.schemas.detection import DetectionResponse
from app.services.detection_service import run_ppe_detection
from app.api.deps import get_db

router = APIRouter()

@router.post("/analyze", response_model=DetectionResponse)
async def analyze_frame(image: UploadFile = File(...), db: Session = Depends(get_db)):
    image_bytes = await image.read()
    return run_ppe_detection(image_bytes, db)