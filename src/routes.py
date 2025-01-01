"""_summary_
"""
from fastapi import APIRouter
from .services import list_all_tasks

router = APIRouter()

@router.get("/")
async def get_all_tasks():
    return list_all_tasks()

@router.get("/{id}")
async def get_task_by_id(id: int):
    return {"message": f'Task {id}'}
