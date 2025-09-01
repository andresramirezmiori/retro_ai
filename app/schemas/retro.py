from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from app.models.retro import RetroStatus


class RetroBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: RetroStatus = RetroStatus.CREATED
    column_mapping: Optional[dict] = None


class RetroCreate(RetroBase):
    pass


class RetroUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[RetroStatus] = None
    column_mapping: Optional[dict] = None


class RetroOut(RetroBase):
    id: int
    identifier: str = Field(..., description="UUID identifier")

    model_config = dict(from_attributes=True)

