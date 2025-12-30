from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.user import User
import random


def get_tasks_for_stage(db: Session, project_id: int, stage: int):
  return (
    db.query(Task)
    .filter(
      Task.project_id == project_id,
      Task.stage == stage
    )
    .all()
  )


def match_tasks_by_keywords(tasks, user_response: str):
  matched = []
  user_response = user_response.lower()

  for task in tasks:
    if not task.keywords:
      continue

  keywords = [kw.strip().lower() for kw in task.keywords.split(",")]
  if any(keyword in user_response for keyword in keywords):
    matched.append(task)

  return matched


def update_user_score(user: User, score: int, db: Session):
  user.t_score += score
  db.commit()
  db.refresh(user)
  return user.t_score


def play_stage(db: Session, user_id: int, project_id: int, stage: int, user_response: str):
  user = db.query(User).filter(User.id == user_id).first()
  if not user:
    return {"error": "User not found"}

  tasks = get_tasks_for_stage(db, project_id, stage)
  if not tasks:
    return {"message": "No tasks available for this stage"}

  matched_tasks = match_tasks_by_keywords(tasks, user_response)

  # Choose matched task if exists, else fallback
  selected_task = random.choice(matched_tasks or tasks)

  score_awarded = selected_task.score if selected_task in matched_tasks else 0
  total_score = update_user_score(user, score_awarded, db)

  return {
    "task_text": selected_task.text,
    "matched": selected_task in matched_tasks,
    "score_awarded": score_awarded,
    "total_score": total_score,
    "next_stage": stage + 1
  }