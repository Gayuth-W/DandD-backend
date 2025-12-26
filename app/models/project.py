from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Project(Base):
  __tablename__ = "projects"
  
  id=Column(Integer, primary_key=True, index=True)
  name=Column(String, index=True, nullable=False)
  owner_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  owner=relationship("User", back_populates="project")
  tasks=relationship(
    "Task",
    back_populates="project",
    cascade="all, delete"
    )