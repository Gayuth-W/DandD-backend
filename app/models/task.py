from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    score = Column(Integer, default=0)
    project_id = Column(Integer,ForeignKey("projects.id", ondelete="CASCADE"),nullable=False)

    project = relationship(
        "Project",
        back_populates="tasks"
    )