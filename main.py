from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import db_get
from database import SessionLocal, engine
from models import Base, Task
import psycopg2
from psycopg2.extras import RealDictCursor

from schemas import TaskCreate, TaskUpdate, TaskOut

Base.metadata.create_all(bind=engine)

app = FastAPI()

try:
  conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="NLRM", cursor_factory=RealDictCursor)
  cursor = conn.cursor()
  print("Database connection successful")
except Exception as e:
  print(f"Error connecting to the database: {e}")


@app.post("/tasks/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(db_get)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[TaskOut])
def read_tasks(db: Session = Depends(db_get)):
    return db.query(Task).all()

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(db_get)):
    db_task = db.query(Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(db_get)):
    db_task = db.query(Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}
