from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, data: TaskCreate):
  task = Task(**data.dict())
  db.add(task)
  db.commit()
  db.refresh(task)
  return task

def get_task(db: Session, task_id: int):
  task = db.get(Task, task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  return task

def get_tasks(db: Session):
  return db.query(Task).all()

def update_task(db: Session, task_id: int, data: TaskUpdate):
  task = get_task(db, task_id)
  for key, value in data.dict(exclude_unset=True).items():
    setattr(task, key, value)
  db.commit()
  db.refresh(task)
  return task

def delete_task(db: Session, task_id: int):
  task = get_task(db, task_id)
  db.delete(task)
  db.commit()
  return "task deleted"