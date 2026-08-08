from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertCreate(BaseModel):
    type: str
    message: str
    severity: str

class AlertOut(BaseModel):
    id: int
    type: str
    message: str
    severity: str
    created_at: datetime
    resolved: bool

    class Config:
        from_attributes = True