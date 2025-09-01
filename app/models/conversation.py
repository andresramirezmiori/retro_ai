from __future__ import annotations

from typing import List

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    retro_id: Mapped[int] = mapped_column(ForeignKey("retros.id"), nullable=False, index=True)
    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.id"), nullable=False, index=True
    )

    retro: Mapped["Retro"] = relationship(back_populates="conversations")
    participant: Mapped["Participant"] = relationship(back_populates="conversations")
    messages: Mapped[List["Message"]] = relationship(
        back_populates="conversation", cascade="all, delete-orphan"
    )


from app.models.retro import Retro  # noqa: E402
from app.models.participant import Participant  # noqa: E402
from app.models.message import Message  # noqa: E402

