from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class ParticipantBase(BaseModel):
    name: str
    role: Optional[str] = None
    is_admin: bool = False


class ParticipantCreate(ParticipantBase):
    retro_id: int


class ParticipantOut(ParticipantBase):
    id: int
    retro_id: int

    model_config = dict(from_attributes=True)

