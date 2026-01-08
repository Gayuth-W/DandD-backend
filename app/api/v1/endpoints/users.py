from app.core.deps import get_current_admin
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserOut, UserBase
from app.repo.UserRepository import (
  create_user, get_user, get_users, update_user, delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create(data: UserBase, db: Session = Depends(get_db)):
  return create_user(db, data)

@router.get("/{user_id}", response_model=UserOut)
def read(user_id: int, db: Session = Depends(get_db)):
  return get_user(db, user_id)

@router.get("/", response_model=list[UserOut])
def read_all(db: Session = Depends(get_db), admin: dict = Depends(get_current_admin)):
  return get_users(db)

@router.put("/{user_id}", response_model=UserOut)
def update(user_id: int, data: UserUpdate, db: Session = Depends(get_db), admin: dict = Depends(get_current_admin)):
  return update_user(db, user_id, data)

@router.delete("/{user_id}", status_code=204)
def delete(user_id: int, db: Session = Depends(get_db), admin: dict = Depends(get_current_admin)):
  delete_user(db, user_id)
  return {"detail": "User deleted"}