from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    retro_item_id: Mapped[int] = mapped_column(
        ForeignKey("retro_items.id"), nullable=False, index=True
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)

    retro_item: Mapped["RetroItem"] = relationship(back_populates="comments")


from app.models.retro_item import RetroItem  # noqa: E402

