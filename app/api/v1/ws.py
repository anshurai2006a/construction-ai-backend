from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws/live")
async def live_feed(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"echo: {data}")
    except Exception:
        await websocket.close()