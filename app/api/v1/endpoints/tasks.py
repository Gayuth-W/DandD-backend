from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.repo.TaskRepository import (
  create_task, get_task, get_tasks, update_task, delete_task
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def create(data: TaskCreate, db: Session = Depends(get_db)):
  return create_task(db, data)

@router.get("/{task_id}", response_model=TaskOut)
def read(task_id: int, db: Session = Depends(get_db)):
  return get_task(db, task_id)

@router.get("/", response_model=list[TaskOut])
def read_all(db: Session = Depends(get_db)):
  return get_tasks(db)

@router.put("/{task_id}", response_model=TaskOut)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
  return update_task(db, task_id, data)

@router.delete("/{task_id}", status_code=204)
def delete(task_id: int, db: Session = Depends(get_db)):
  delete_task(db, task_id)
  return {"detail": "Task deleted"}