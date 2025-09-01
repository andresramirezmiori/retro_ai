from __future__ import annotations

from datetime import date
from typing import Optional

from sqlalchemy import Boolean, Date, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ActionItem(Base):
    __tablename__ = "action_items"
    __table_args__ = (
        UniqueConstraint("retro_item_id", name="uq_actionitem_retroitem_one_to_one"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    retro_item_id: Mapped[int] = mapped_column(ForeignKey("retro_items.id"), nullable=False)
    assigned_to_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("participants.id"), nullable=True
    )

    closed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    comments: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    retro_item: Mapped["RetroItem"] = relationship(back_populates="action_item")
    assignee: Mapped[Optional["Participant"]] = relationship(
        back_populates="assigned_action_items"
    )


from app.models.retro_item import RetroItem  # noqa: E402
from app.models.participant import Participant  # noqa: E402

