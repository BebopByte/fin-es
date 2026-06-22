from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, UTC

from app.db.base import Base

class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)

    ticker: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        index=True,
        nullable=False        
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    industry: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC)
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC)   
    )