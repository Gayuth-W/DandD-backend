from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base

class Admin(Base):
  __tablename__ = "admins"
  
  id=Column(Integer, primary_key=True, index=True)
  username=Column(String, unique=True, index=True, nullable=False)
  password_hash=Column(String, nullable=False)
  is_active=Column(Boolean, default=True)