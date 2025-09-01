from __future__ import annotations

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    retro_id: int
    participant_id: int


class ConversationOut(BaseModel):
    id: int
    retro_id: int
    participant_id: int

    model_config = dict(from_attributes=True)

