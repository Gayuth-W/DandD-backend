from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

def create_user(db: Session, data: UserCreate):
  user = User(email=data.email, project_id=data.project_id)
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user(db: Session, user_id: int):
  user = db.get(User, user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user

def get_users(db: Session):
  return db.query(User).all()

def update_user(db: Session, user_id: int, data: UserUpdate):
  user = get_user(db, user_id)
  for key, value in data.dict(exclude_unset=True).items():
    setattr(user, key, value)
  db.commit()
  db.refresh(user)
  return user

def delete_user(db: Session, user_id: int):
  user = get_user(db, user_id)
  db.delete(user)
  db.commit()
  return "user deleted"