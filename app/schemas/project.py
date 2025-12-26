from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    owner_id: int

class ProjectOut(ProjectBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
        
class ProjectUpdate(BaseModel):
    name: str | None = None        