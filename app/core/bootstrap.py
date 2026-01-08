import os
from sqlalchemy import orm
from app.models.admin import Admin
from app.core.security import hash_password
from dotenv import load_dotenv
load_dotenv()
def create_admin_if_not_exists(db: orm.Session):
  admin_exists=db.query(Admin).first()
  if admin_exists:
    return
  
  admin=Admin(
    username=os.getenv("ADMIN_USERNAME"),
    password_hash=hash_password(os.getenv("ADMIN_PASSWORD")),
    must_change_password=True,
    is_active=True
  )
  
  db.add(admin)
  db.commit()