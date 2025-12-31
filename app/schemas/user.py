from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    project_id: int

class UserCreate(UserBase):
    project_id: int

class UserOut(BaseModel):
    id: int
    email: str
    project_id: int
    t_score: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    
class ProjectUpdate(BaseModel):
    name: str | None = None
    