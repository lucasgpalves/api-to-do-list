"""_summary_
"""
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .queries import (
    query_select_tasks, 
    query_select_task_by_id, 
    query_select_task_by_state,
    query_paginate_task,
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

async def list_tasks_by_state(session: Session, state: str) -> List[Dict]:
    try:
        data = query_select_task_by_state(session, state)
        return data
    finally:
        session.close()
        
async def list_tasks_per_page(session: Session, skip: int = 0, limit: int = 10):
    try:
        data = query_paginate_task(session, skip, limit)
        return data
    finally:
        session.close()
        
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