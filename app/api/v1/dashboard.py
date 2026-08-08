from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.deps import get_db
from app.models.alert import Alert
from app.models.detection_event import DetectionEvent

router = APIRouter()

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    total_alerts = db.query(func.count(Alert.id)).scalar()
    unresolved = db.query(func.count(Alert.id)).filter(Alert.resolved == False).scalar()
    total_detections = db.query(func.count(DetectionEvent.id)).scalar()

    return {
        "total_alerts": total_alerts,
        "unresolved_alerts": unresolved,
        "total_detections": total_detections,
    }