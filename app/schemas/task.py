from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    project_id: int

class TaskOut(TaskBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True
        
class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None