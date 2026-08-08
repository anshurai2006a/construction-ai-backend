from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.schemas.alert import AlertCreate

def create_alert(alert_in: AlertCreate, user_id: int | None, db: Session) -> Alert:
    alert = Alert(
        type=alert_in.type,
        message=alert_in.message,
        severity=alert_in.severity,
        user_id=user_id,
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

def get_all_alerts(db: Session, resolved: bool | None = None) -> list[Alert]:
    query = db.query(Alert)
    if resolved is not None:
        query = query.filter(Alert.resolved == resolved)
    return query.order_by(Alert.created_at.desc()).all()

def resolve_alert(alert_id: int, db: Session) -> Alert | None:
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if alert:
        alert.resolved = True
        db.commit()
        db.refresh(alert)
    return alert