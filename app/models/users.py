import datetime

from sqlalchemy import Integer, String, TIMESTAMP, Column, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.mutable import MutableList
from app.db.base import Base
from app.db.data_base import engine


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    data_conversation: Mapped[list] = mapped_column(MutableList.as_mutable(JSON), nullable=True)
    role: Mapped[str] = mapped_column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now(datetime.UTC))


Base.metadata.create_all(engine)
