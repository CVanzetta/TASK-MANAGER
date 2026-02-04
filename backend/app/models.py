from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone
from .db import Base


def get_utc_now():
    return datetime.now(timezone.utc)


# Task status constants
STATUS_TODO = "TODO"
STATUS_DOING = "DOING"
STATUS_DONE = "DONE"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default=STATUS_TODO)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=get_utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=get_utc_now)
