from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Users(Base):
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(25))
