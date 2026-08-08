from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.alert import AlertCreate, AlertOut
from app.services.alert_service import create_alert, get_all_alerts, resolve_alert
from app.api.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=AlertOut)
def create(alert_in: AlertCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_alert(alert_in, current_user.id, db)

@router.get("/", response_model=List[AlertOut])
def list_alerts(resolved: Optional[bool] = None, db: Session = Depends(get_db)):
    return get_all_alerts(db, resolved)

@router.patch("/{alert_id}/resolve", response_model=AlertOut)
def resolve(alert_id: int, db: Session = Depends(get_db)):
    return resolve_alert(alert_id, db)