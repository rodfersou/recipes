
from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RecipeSA(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[Optional[datetime]]
    updated_at: Mapped[Optional[datetime]]
    title: Mapped[str] = mapped_column(String(100))
    making_time: Mapped[str] = mapped_column(String(100))
    serves: Mapped[str] = mapped_column(String(100))
    ingredients: Mapped[str] = mapped_column(String(300))
    cost: Mapped[int] = mapped_column(Integer)
