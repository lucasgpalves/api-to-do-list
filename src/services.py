"""_summary_
"""
from fastapi import HTTPException
from .connection_db import ConnectionDB
from .queries import (
    query_select_tasks, 
    query_select_task_by_id, 
    query_insert_task,
    query_update_task_by_id,
    query_delete_task_by_id
)
from typing import List, Dict
from .models import Task, TaskCreate, TaskUpdate
from psycopg2.extras import RealDictCursor

def make_connection():
    conn = ConnectionDB.init_connection()
    return conn

async def list_all_tasks() -> List[Dict]:
    conn = make_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            data = query_select_tasks(cur)
            return data
    finally:
        conn.close()
        
async def list_task_by_id(id: int) -> Dict:
    conn = make_connection()
    try: 
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            data = query_select_task_by_id(cur, id)
            return data
    finally:
        conn.close()
        
async def create_task(task: Task):
    conn = make_connection()
    try: 
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            data = query_insert_task(cur, task)
            conn.commit()
            return data
    finally:
        conn.close()
        
async def update_task_by_id(id: int, task: TaskUpdate):
    conn = make_connection()
    try: 
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            data = query_update_task_by_id(cur, id, task)
            conn.commit()
            return data
    finally:
        conn.close()
        
async def remove_task_by_id(id: int):
    conn = make_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            task_deleted = query_delete_task_by_id(cur, id)
            conn.commit()
            if not task_deleted:
                raise HTTPException(status_code=404, detail="Task not found")
            return {"message": "Task deleted"}
    finally:
        conn.close()