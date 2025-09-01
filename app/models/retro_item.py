from __future__ import annotations

import enum
from typing import List, Optional

from sqlalchemy import Boolean, Enum, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RetroItemType(str, enum.Enum):
    to_improve = "to_improve"
    to_stop = "to_stop"
    to_continue = "to_continue"


class RetroItem(Base):
    __tablename__ = "retro_items"
    __table_args__ = (
        UniqueConstraint("retro_id", "retro_identifier", name="uq_retro_item_identifier_per_retro"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    retro_id: Mapped[int] = mapped_column(ForeignKey("retros.id"), nullable=False, index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("participants.id"), nullable=False)

    type: Mapped[RetroItemType] = mapped_column(Enum(RetroItemType), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_action_item: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    retro_identifier: Mapped[int] = mapped_column(Integer, nullable=False)

    # self-reference for merges
    merged_into_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("retro_items.id"), nullable=True
    )

    retro: Mapped["Retro"] = relationship(back_populates="items", foreign_keys=[retro_id])
    owner: Mapped["Participant"] = relationship(back_populates="items_owned")
    merged_into: Mapped[Optional["RetroItem"]] = relationship(remote_side=[id])
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="retro_item", cascade="all, delete-orphan"
    )
    action_item: Mapped[Optional["ActionItem"]] = relationship(
        back_populates="retro_item", uselist=False, cascade="all, delete-orphan"
    )


from app.models.retro import Retro  # noqa: E402
from app.models.participant import Participant  # noqa: E402
from app.models.comment import Comment  # noqa: E402
from app.models.action_item import ActionItem  # noqa: E402

