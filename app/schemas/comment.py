from __future__ import annotations

from pydantic import BaseModel


class CommentCreate(BaseModel):
    retro_item_id: int
    content: str


class CommentOut(BaseModel):
    id: int
    retro_item_id: int
    content: str

    model_config = dict(from_attributes=True)

