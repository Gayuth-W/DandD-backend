from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.project import Project
from app.schemas.project import ProjectBase, ProjectCreate, ProjectUpdate

def create_project(db: Session, data: ProjectBase):
  project = Project(**data.dict())
  db.add(project)
  db.commit()
  db.refresh(project)
  return project

def get_project(db: Session, project_id: int):
  project = db.get(Project, project_id)
  if not project:
    raise HTTPException(status_code=404, detail="Project not found")
  return project

def get_projects(db: Session):
  return db.query(Project).all()

def update_project(db: Session, project_id: int, data: ProjectUpdate):
  project = get_project(db, project_id)
  for key, value in data.dict(exclude_unset=True).items():
    setattr(project, key, value)
  db.commit()
  db.refresh(project)
  return project

def delete_project(db: Session, project_id: int):
  project = get_project(db, project_id)
  db.delete(project)
  db.commit()
  return "project deleted"