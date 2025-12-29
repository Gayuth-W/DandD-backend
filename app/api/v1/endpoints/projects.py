from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.schemas.project import ProjectBase, ProjectCreate, ProjectUpdate, ProjectOut
from app.services.project_service import (
  create_project, get_project, get_projects, update_project, delete_project
)

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectBase)
def create(data: ProjectBase, db: Session = Depends(get_db)):
  return create_project(db, data)

@router.get("/{project_id}", response_model=ProjectOut)
def read(project_id: int, db: Session = Depends(get_db)):
  return get_project(db, project_id)

@router.get("/", response_model=list[ProjectOut])
def read_all(db: Session = Depends(get_db)):
  return get_projects(db)

@router.put("/{project_id}", response_model=ProjectOut)
def update(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db)):
  return update_project(db, project_id, data)

@router.delete("/{project_id}", status_code=204)
def delete(project_id: int, db: Session = Depends(get_db)):
  delete_project(db, project_id)
  return {"detail": "Project deleted"}