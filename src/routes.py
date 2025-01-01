"""_summary_
"""
from fastapi import APIRouter, Depends
from .services import (
    list_all_tasks, 
    list_task_by_id, 
    create_task, 
    update_task_by_id,
    remove_task_by_id,
    # generate_token
)
from .authentication import authenticate, generate_jwt
from .models import TaskCreate, TaskUpdate, Task
from typing import List

router = APIRouter()

@router.get("/token")
async def get_token():
    return {"token": generate_jwt()}

@router.get("/")
async def get_all_tasks(auth: dict = Depends(authenticate)):
    return await list_all_tasks()

@router.get("/{id}")
async def get_task_by_id(id: int, auth: dict = Depends(authenticate)):
    return await list_task_by_id(id)

@router.post("/", response_model=Task)
async def post_new_task(task: TaskCreate, auth: dict = Depends(authenticate)):
    return await create_task(task)

@router.put("/{id}", response_model=Task)
async def put_task_by_id(id: int,task: TaskUpdate, auth: dict = Depends(authenticate)):
    return await update_task_by_id(id, task)

@router.delete("/{id}", response_model=dict)
async def delete_task_by_id(id: int, auth: dict = Depends(authenticate)):
    return await remove_task_by_id(id)
