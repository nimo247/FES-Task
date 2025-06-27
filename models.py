from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status:bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: bool = False

class TaskOut(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    created_at: datetime
    status: bool =False

class RegisterModel(BaseModel):
    username: str
    password: str

class LoginModel(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str
    token: str
