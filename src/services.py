"""_summary_
"""
from .connection_db import ConnectionDB
from .queries import query_select_tasks, query_select_task_by_id
from typing import List, Dict

def make_connection():
    conn = ConnectionDB.init_connection()
    return conn

def list_all_tasks() -> List[Dict]:
    conn = make_connection()
    try:
        with conn.cursor() as cur:
            data = query_select_tasks(cur)
            tasks = convert_data(data)
            return tasks
    finally:
        conn.close()
        
def list_task_by_id(id: int) -> Dict:
    conn = make_connection()
    try: 
        with conn.cursor() as cur:
            data = query_select_task_by_id(id)
            task = convert_data(data)
            return task
    finally:
        conn.close()
        
def convert_data(data):
    # Formatar os dados para o formato desejado
    tasks = []
    for task in data:
        formatted_task = {
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "state": task[3],
            "created_at": task[4],
            "updated_at": task[5],
        }
        tasks.append(formatted_task)
        
    return tasks
