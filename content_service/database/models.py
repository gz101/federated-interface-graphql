from sqlalchemy import Column, Integer, String
from content_service.database.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    contentMessage = Column(String, index=True)
