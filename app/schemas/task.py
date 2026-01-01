from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    # completed: bool = False

class TaskCreate(TaskBase):
    project_id: int
    text: str
    score: int
    stage: int
    keywords: str
    is_default: bool = False

class TaskOut(TaskBase):
    id: int
    project_id: int
    text: str
    score: int
    stage: int
    keywords: str
    is_default: bool

    class Config:
        from_attributes = True
        
class TaskUpdate(BaseModel):
    title: str | None = None
    project_id: int
    text: str
    score: int
    stage: int
    keywords: str