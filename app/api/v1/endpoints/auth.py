# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.admin import Admin
from app.core.security import verify_password, hash_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/admin/login")
def admin_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    admin = db.query(Admin).filter(
        Admin.username == form_data.username
    ).first()

    if not admin or not verify_password(form_data.password, admin.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": admin.username,
        "role": "admin"
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

from pydantic import BaseModel

class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str

@router.post("/admin/change-password")
def change_password(
    data: ChangePasswordSchema,
    db: Session = Depends(get_db),
):
    admin = db.query(Admin).first()

    if not verify_password(data.old_password, admin.password_hash):
        raise HTTPException(status_code=401, detail="Wrong password")

    admin.password_hash = hash_password(data.new_password)
    admin.must_change_password = False
    db.commit()

    return {"message": "Password changed successfully"}
