from sqlalchemy.orm import Session
from app.models.task import Task

def get_tasks_by_project(project_id: int, db: Session):
  """
  This function will fetch all tasks for a given project and organize them by their stages.
  """
  tasks = db.query(Task).filter(Task.project_id == project_id).all()
  stages = {}
  for task in tasks:
    if task.stage not in stages:
      stages[task.stage] = []
    stages[task.stage].append(task)
  
  return stages