from pydantic import BaseModel
from typing import List

class DetectionResult(BaseModel):
    label: str
    confidence: float
    bbox: List[float]

class DetectionResponse(BaseModel):
    detections: List[DetectionResult]
    alert_triggered: bool