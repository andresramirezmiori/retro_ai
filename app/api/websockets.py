from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter()

active_connections: List[WebSocket] = []


@router.websocket("/ws/retro/{retro_id}")
async def chat_endpoint(websocket: WebSocket, retro_id: str):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Echo back for testing
            await websocket.send_text(f"Confesionario te responde: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
