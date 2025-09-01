from __future__ import annotations

from typing import Optional
from pydantic import BaseModel

from app.models.retro_item import RetroItemType


class RetroItemBase(BaseModel):
    type: RetroItemType
    content: str
    is_action_item: bool = False
    retro_identifier: int


class RetroItemCreate(RetroItemBase):
    retro_id: int
    owner_id: int


class RetroItemOut(RetroItemBase):
    id: int
    retro_id: int
    owner_id: int
    merged_into_id: Optional[int] = None

    model_config = dict(from_attributes=True)

