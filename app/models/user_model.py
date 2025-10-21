from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.config.database import Base
from sqlalchemy.sql import func


class User(Base):

    __tablename__ = "users"

    id = Column(Integer,  primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())




    def __repr__(self):
        return f"<User(id = {self.id}, username= '{self.username}', email = '{self.email}')>"


