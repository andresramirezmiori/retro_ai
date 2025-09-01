from __future__ import annotations

from datetime import date
from typing import Optional
from pydantic import BaseModel


class ActionItemBase(BaseModel):
    closed: bool = False
    due_date: Optional[date] = None
    content: str
    comments: Optional[str] = None


class ActionItemCreate(ActionItemBase):
    retro_item_id: int
    assigned_to_id: Optional[int] = None


class ActionItemUpdate(BaseModel):
    closed: Optional[bool] = None
    due_date: Optional[date] = None
    content: Optional[str] = None
    comments: Optional[str] = None
    assigned_to_id: Optional[int] = None


class ActionItemOut(ActionItemBase):
    id: int
    retro_item_id: int
    assigned_to_id: Optional[int] = None

    model_config = dict(from_attributes=True)

