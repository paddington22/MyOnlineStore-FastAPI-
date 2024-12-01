from enum import Enum

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    title: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    unit_price: Mapped[float] = mapped_column(Float(2, asdecimal=True), nullable=False)
