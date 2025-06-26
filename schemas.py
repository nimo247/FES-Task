from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    filter: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    filter: bool = False

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    filter: bool = False

    class Config:
        from_attributes = True  # replaces orm_mode
