from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Project(Base):
  __tablename__ = "projects"
  
  id=Column(Integer, primary_key=True, index=True)
  name=Column(String, index=True, nullable=False)
  text=Column(String, nullable=False)
  
  users=relationship(
    "User", 
    back_populates="project",
    cascade="all, delete-orphan"
  )
  tasks=relationship(
    "Task",
    back_populates="project",
    cascade="all, delete-orphan"
    )