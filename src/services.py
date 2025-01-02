"""_summary_
"""
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .queries import (
    query_select_tasks, 
    query_select_task_by_id, 
    query_insert_task,
    query_update_task_by_id,
    query_delete_task_by_id
)
from .models import Task, TaskCreate, TaskUpdate
from typing import List, Dict

async def list_all_tasks(session: Session) -> List[Dict]:
    try:
        data = query_select_tasks(session)
        return data
    finally:
        session.close()
        
async def list_task_by_id(session: Session, id: int) -> Dict:
    data = query_select_task_by_id(session, id)
    if not data:
        raise HTTPException(status_code=404, detail="Task not found")
    return data
        
async def create_task(session: Session, task: TaskCreate):
    data = query_insert_task(session, task)
    return data
        
async def update_task_by_id(session: Session, id: int, task: TaskUpdate):
    data = query_update_task_by_id(session, id, task)
    if not data:
        raise HTTPException(status_code=404, detail=f"Task not found {data}")
    return data
        
async def remove_task_by_id(session: Session, id: int):
    data = query_delete_task_by_id(session, id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Task not found {data}")
    return {"message": "Task deleted"}