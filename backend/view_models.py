from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime

class JobBase(BaseModel):
    title: str
    company: str
    company_url: Optional[str] = None
    location: Optional[str] = 'Remote'
    description: str
    posted_date: Optional[date] = datetime.now().date()
    is_active: Optional[bool] = True

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    pass


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False

class User(UserBase):
    id: int
    jobs: List[Job] = []

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str


