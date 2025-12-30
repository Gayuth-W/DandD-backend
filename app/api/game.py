from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.endpoints import projects
from app.core.database import get_db
from app.schemas import game
from app.schemas.game import PlayStageRequest, PlayStageResponse
from app.services.game_service import play_stage
from app.models.user import User

router = APIRouter(prefix="/game", tags=["Game"])
# router.include_router(game.router)      # /game endpoints
# router.include_router(projects.router)

@router.post("/play", response_model=PlayStageResponse)
def play_game(payload: PlayStageRequest, db: Session = Depends(get_db)):
    result = play_stage(
        db=db,
        user_id=payload.user_id,
        project_id=payload.project_id,
        user_response=payload.user_response
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

@router.get("/state")
def game_state(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "current_stage": user.current_stage,
        "total_score": user.t_score,
        "completed": user.current_stage > 7
    }

@router.post("/reset")
def reset_game(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.t_score = 0
    user.current_stage = 1
    db.commit()

    return {"message": "Game reset successful"}
