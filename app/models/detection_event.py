from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from app.db.base import Base

class DetectionEvent(Base):
    __tablename__ = "detection_events"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)          # e.g. "no_helmet"
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)