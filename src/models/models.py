from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, nullable=False)
    first_name = mapped_column(String, nullable=False)


class Wish(Base):
    __tablename__ = "wish"

    STATUS = (
        ('COMPLETE', 'complete'),
        ('NOT COMPLETE', 'not complete'),
    )

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(length=40), nullable=False)
    description = mapped_column(String, nullable=True)
    created_at = mapped_column(TIMESTAMP, default=datetime.utcnow())
    status = mapped_column(ChoiceType(STATUS), default="NOT COMPLETE")
    user_id = mapped_column(Integer, ForeignKey('user.id'))
