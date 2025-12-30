from fastapi import APIRouter, Depends
from app.api.v1.endpoints import users, projects, tasks
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.game_service import play_stage

router = APIRouter()
router.include_router(users.router)
router.include_router(projects.router)
router.include_router(tasks.router)

@router.post("/play")
def play(user_id: int, project_id: int, stage: int, user_input: str, db: Session = Depends(get_db)):
  return play_stage(db, user_id, project_id, stage, user_input)