from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import every model here so Alembic and Base.metadata.create_all() can see them
from app.models.user import User
from app.models.alert import Alert
from app.models.detection_event import DetectionEvent
from app.models.document import Document