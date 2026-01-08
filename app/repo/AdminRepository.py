from .base import BaseRepository
from app.models.Admin import Admin
from sqlalchemy.orm import Session
from app.schemas.admin import AdminCreate

def create_admin(db: Session, admin: AdminCreate) -> Admin:
  db_admin = Admin(
    username=admin.username,
    password_hash=admin.password_hash,
    is_active=admin.is_active
  )
  db.add(db_admin)
  db.commit()
  db.refresh(db_admin)
  return db_admin 
  
