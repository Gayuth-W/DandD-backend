from sqlalchemy.orm import Session
from app.models.task import Task
import random
from app.models.user import User

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

def select_task_for_stage(stage: int, stages: dict):
  """
  This function selects a random task from the specified stage.
  """
  if stage in stages and stages[stage]:
    return random.choice(stages[stage])
  
  return None

def check_user_response(user_response: str, task_keywords: str):
  """
  This function checks if the user's response contains any of the keywords for the task.
  """
  if not task_keywords:
      return False
  
  keywords = [kw.strip().lower() for kw in task_keywords.split(",")]
  user_words = user_response.lower().split()
  
  return any(word in keywords for word in user_words)

def update_user_score(user: User, score: int, db: Session):
  """
  Add score to user's total score.
  """
  user.t_score += score
  db.commit()
  db.refresh(user)
  return user.t_score

def play_stage(user: User, project_id: int, stage: int, user_response: str, db: Session):
  stages = get_tasks_by_project(project_id, db)
  
  task = select_task_for_stage(stage, stages)
  if not task:
    return {"message": "No tasks available for this stage."}
  
  matched = check_user_response(user_response, task.keywords)
  
  score = task.score if matched else 0
  updated_score = update_user_score(user, score, db)
  
  return {
    "task_text": task.text,
    "matched": matched,
    "score_awarded": score,
    "total_score": updated_score,
    "next_stage": stage + 1
  }