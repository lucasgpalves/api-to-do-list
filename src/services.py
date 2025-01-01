"""_summary_
"""
from .connection_db import ConnectionDB
from .queries import query_select_tasks, query_select_task_by_id, query_insert_task
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
        