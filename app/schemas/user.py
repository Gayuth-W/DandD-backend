from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    project_id: int

class UserCreate(UserBase):
    project_id: int

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    
class ProjectUpdate(BaseModel):
    name: str | None = None
    