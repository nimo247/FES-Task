from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RegisterModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=10)
    password: str = Field(..., min_length=6)

class LoginModel(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    token: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status:bool = False 

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: bool = False 

from typing import Optional

class TaskOut(BaseModel):
    id: str
    title: str
    description: str
    created_at: datetime
    status: bool=False 