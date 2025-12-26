from fastapi import APIRouter
from app.api.v1.endpoints import users, projects, tasks

router = APIRouter()
router.include_router(users.router)
router.include_router(projects.router)
router.include_router(tasks.router)