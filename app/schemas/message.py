from __future__ import annotations

from pydantic import BaseModel

from app.models.message import MessageType


class MessageCreate(BaseModel):
    conversation_id: int
    content: str
    type: MessageType


class MessageOut(BaseModel):
    id: int
    conversation_id: int
    content: str
    type: MessageType

    model_config = dict(from_attributes=True)

