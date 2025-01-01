"""_summary_
"""
from fastapi import APIRouter
from .services import list_all_tasks, list_task_by_id, create_task
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