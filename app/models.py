from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)  # e.g., 'admin', 'user', etc.
    status = Column(String, index=True, nullable=False)  # e.g., 'active', 'inactive'
