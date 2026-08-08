from sqlalchemy.orm import Session
from app.ai.ppe_detector import detect_ppe
from app.models.detection_event import DetectionEvent
from app.schemas.detection import DetectionResponse

ALERT_LABELS = {"no_helmet", "no_vest"}
CONFIDENCE_THRESHOLD = 0.6

def run_ppe_detection(image_bytes: bytes, db: Session) -> DetectionResponse:
    detections = detect_ppe(image_bytes)

    alert_triggered = False
    for d in detections:
        if d["label"] in ALERT_LABELS and d["confidence"] >= CONFIDENCE_THRESHOLD:
            alert_triggered = True

        # log every detection event for analytics/dashboard
        event = DetectionEvent(label=d["label"], confidence=d["confidence"])
        db.add(event)

    db.commit()

    return DetectionResponse(detections=detections, alert_triggered=alert_triggered)