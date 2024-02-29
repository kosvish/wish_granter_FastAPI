from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, MetaData, Table
from fastapi_users.db import SQLAlchemyBaseUserTable
from src.database import Base


# class User(SQLAlchemyBaseUserTable[int], Base):
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     username = Column(String, nullable=False)
#     registered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     hashed_password: str = Column(String(length=1024), nullable=False)
#     is_active: bool = Column(Boolean, default=True, nullable=False)
#     is_superuser: bool = Column(Boolean, default=False, nullable=False)
#     is_verified: bool = Column(Boolean, default=False, nullable=False)
