from app.core.middleware import LogRequestsMiddleware
from app.core.rate_limit import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.db.base import Base
from app.db.session import engine

from app.api.v1 import auth, detection, rag, voice, alerts, dashboard, ws

# Creates tables from models on startup (fine for dev; use Alembic for production changes)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Construction Co-Pilot API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LogRequestsMiddleware)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(detection.router, prefix="/api/v1/detection", tags=["detection"])
app.include_router(rag.router, prefix="/api/v1/rag", tags=["rag"])
app.include_router(voice.router, prefix="/api/v1/voice", tags=["voice"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["alerts"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"])
app.include_router(ws.router, tags=["websocket"])

@app.get("/")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)