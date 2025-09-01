from __future__ import annotations

from typing import List, Optional

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    retro_id: Mapped[int] = mapped_column(ForeignKey("retros.id"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # diagram: rol
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    retro: Mapped["Retro"] = relationship(back_populates="participants")
    conversations: Mapped[List["Conversation"]] = relationship(
        back_populates="participant", cascade="all, delete-orphan"
    )
    items_owned: Mapped[List["RetroItem"]] = relationship(
        back_populates="owner"
    )
    assigned_action_items: Mapped[List["ActionItem"]] = relationship(
        back_populates="assignee"
    )


from app.models.retro import Retro  # noqa: E402
from app.models.conversation import Conversation  # noqa: E402
from app.models.retro_item import RetroItem  # noqa: E402
from app.models.action_item import ActionItem  # noqa: E402

