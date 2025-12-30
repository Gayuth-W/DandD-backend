import random
from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.user import User
from app.core.constants import MAX_STAGE


def get_tasks_for_stage(db: Session, project_id: int, stage: int):
    return (
        db.query(Task)
        .filter(
            Task.project_id == project_id,
            Task.stage == stage
        )
        .all()
    )


def keyword_match(task: Task, user_response: str) -> bool:
    if not task.keywords:
        return False

    keywords = [kw.strip().lower() for kw in task.keywords.split(",")]
    response = user_response.lower()

    return any(keyword in response for keyword in keywords)


def play_stage(
    db: Session,
    user_id: int,
    project_id: int,
    user_response: str
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    # Game already finished
    if user.current_stage > MAX_STAGE:
        return {
            "completed": True,
            "final_score": user.t_score
        }

    tasks = get_tasks_for_stage(db, project_id, user.current_stage)
    if not tasks:
        return {"error": "No tasks configured for this stage"}

    # Match tasks
    matched_tasks = [
        task for task in tasks if keyword_match(task, user_response)
    ]

    selected_task = random.choice(matched_tasks or tasks)
    score_awarded = selected_task.score if selected_task in matched_tasks else 0

    # Update user
    user.t_score += score_awarded
    user.current_stage += 1

    db.commit()
    db.refresh(user)

    completed = user.current_stage > MAX_STAGE

    return {
        "task_text": selected_task.text,
        "matched": selected_task in matched_tasks,
        "score_awarded": score_awarded,
        "total_score": user.t_score,
        "next_stage": user.current_stage,
        "completed": completed
    }
