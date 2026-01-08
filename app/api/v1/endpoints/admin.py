#app/api/v1/endpoints/admin.py
from fastapi import Depends
from app.core.deps import get_current_admin
from fastapi import APIRouter

router = APIRouter()

@router.get("/admin/dashboard")
def dashboard(admin=Depends(get_current_admin)):
  return {"msg": "Welcome admin"}