from __future__ import annotations

import enum
import uuid as uuid_pkg
from typing import List, Optional

from sqlalchemy import Enum, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.database import Base


class RetroStatus(str, enum.Enum):
    CREATED = "CREATED"
    ON_CHARGE = "ON_CHARGE"
    ON_DISCUSS = "ON_DISCUSS"
    CLOSE = "CLOSE"


class Retro(Base):
    __tablename__ = "retros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    identifier: Mapped[str] = mapped_column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid_pkg.uuid4())
    )
    status: Mapped[RetroStatus] = mapped_column(
        Enum(RetroStatus), default=RetroStatus.CREATED, nullable=False
    )
    column_mapping: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    # relationships
    participants: Mapped[List["Participant"]] = relationship(
        back_populates="retro", cascade="all, delete-orphan"
    )
    conversations: Mapped[List["Conversation"]] = relationship(
        back_populates="retro", cascade="all, delete-orphan"
    )
    items: Mapped[List["RetroItem"]] = relationship(
        back_populates="retro", cascade="all, delete-orphan"
    )


# Forward references
from app.models.participant import Participant  # noqa: E402
from app.models.conversation import Conversation  # noqa: E402
from app.models.retro_item import RetroItem  # noqa: E402

