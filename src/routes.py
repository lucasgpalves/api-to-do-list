"""_summary_
"""
from fastapi import APIRouter
from .services import list_all_tasks, list_task_by_id, create_task, update_task_by_id
from .models import TaskCreate, TaskUpdate, Task
from typing import List

router = APIRouter()

@router.get("/")
async def get_all_tasks():
    return await list_all_tasks()

@router.get("/{id}")
async def get_task_by_id(id: int):
    return await list_task_by_id(id)

@router.post("/", response_model=Task)
async def post_new_task(task: TaskCreate):
    return await create_task(task)

@router.put("/{id}", response_model=Task)
async def put_task_by_id(id: int,task: TaskUpdate):
    return await update_task_by_id(id, task)