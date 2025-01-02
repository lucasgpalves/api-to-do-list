"""_summary_
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .connection_db import ConnectionDB
from .services import (
    list_all_tasks, 
    list_task_by_id, 
    create_task, 
    update_task_by_id,
    remove_task_by_id,
)
from .authentication import authenticate, generate_jwt
from .models import TaskCreate, TaskUpdate, TaskResponse
from typing import List

router = APIRouter()

@router.get("/token")
async def get_token():
    return {"token": generate_jwt()}

@router.get("/tasks", response_model=List[TaskResponse])
async def get_all_tasks(auth: dict = Depends(authenticate), session: Session = Depends(ConnectionDB.get_session)):
    return await list_all_tasks(session)

@router.get("/tasks/{id}", response_model=TaskResponse)
async def get_task_by_id(id: int, auth: dict = Depends(authenticate), session: Session = Depends(ConnectionDB.get_session)):
    return await list_task_by_id(session, id)

@router.post("/tasks", response_model=TaskResponse)
async def post_new_task(task: TaskCreate, auth: dict = Depends(authenticate), session: Session = Depends(ConnectionDB.get_session)):
    return await create_task(session, task)

@router.put("/tasks/{id}", response_model=TaskResponse)
async def put_task_by_id(id: int,task: TaskUpdate, auth: dict = Depends(authenticate), session: Session = Depends(ConnectionDB.get_session)):
    return await update_task_by_id(session, id, task)

@router.delete("/tasks/{id}", response_model=dict)
async def delete_task_by_id(id: int, auth: dict = Depends(authenticate), session: Session = Depends(ConnectionDB.get_session)):
    return await remove_task_by_id(session, id)
