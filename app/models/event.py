from sqlalchemy import String, Text, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, UTC

from app.db.base import Base
from app.enums.event_status import EventStatus

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    event_type: Mapped[str] = mapped_column(String(64), index=True)

    title: Mapped[str] = mapped_column(String(255))

    description: Mapped[str | None] = mapped_column(Text)

    status: Mapped[EventStatus] = mapped_column(
        SQLEnum(EventStatus),
        default=EventStatus.PENDING,
        nullable=False,
        index=True,   
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        nullable=False,
    )

    processed_at: Mapped[datetime | None] = mapped_column(
        nullable=True
    )