from __future__ import annotations

import enum
from typing import Optional

from sqlalchemy import Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class MessageType(str, enum.Enum):
    user = "user"
    ai = "ai"


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"), nullable=False, index=True
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[MessageType] = mapped_column(Enum(MessageType), nullable=False)

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")


from app.models.conversation import Conversation  # noqa: E402

