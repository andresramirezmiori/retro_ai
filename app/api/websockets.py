from typing import Dict

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

RetroConnections = Dict[str, Dict[str, WebSocket]]
active_connections: RetroConnections = {}


@router.websocket("/ws/retro/{retro_id}/participant/{participant_id}")
async def chat_endpoint(websocket: WebSocket, retro_id: str, participant_id: str):
    await websocket.accept()
    retro_sockets = active_connections.setdefault(retro_id, {})
    retro_sockets[participant_id] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            # Simple TerapIA echo for now
            await websocket.send_text(
                f"TerapIA te responde (retro {retro_id}, participante {participant_id}): {data}"
            )
    except WebSocketDisconnect:
        pass
    finally:
        retro_sockets = active_connections.get(retro_id)
        if retro_sockets is not None:
            stored_socket = retro_sockets.get(participant_id)
            if stored_socket is websocket:
                retro_sockets.pop(participant_id, None)
                if not retro_sockets:
                    active_connections.pop(retro_id, None)


async def send_to_participant(retro_id: str, participant_id: str, message: str) -> bool:
    """Send a message to a participant if their socket is active."""

    participant_socket = active_connections.get(retro_id, {}).get(participant_id)
    if participant_socket is None:
        return False

    await participant_socket.send_text(message)
    return True
