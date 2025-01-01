"""_summary_
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_tasks():
    return {"message": "All tasks"}

@router.get("/{id}")
async def get_task_by_id(id: int):
    return {"message": f'Task {id}'}
