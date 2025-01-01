from typing import List, Tuple
from .models import Task, TaskCreate, TaskUpdate
from datetime import datetime

def query_select_tasks(cur) -> List[Tuple]:
    query = """
    SELECT 
        id, title, description, state, created_at, updated_at
    FROM
        public.tasks
    ORDER BY id
    """
    
    cur.execute(query)
    data = cur.fetchall()
    return data

def query_select_task_by_id(cur, id: int) -> Tuple:
    query = """
    SELECT 
        id, title, description, state, created_at, updated_at
    FROM
        public.tasks
    WHERE 
        id = %s
    """ 
    
    cur.execute(query, (id, ))
    data = cur.fetchone()
    return data

def query_insert_task(cur, task: TaskCreate):
    query = """
    INSERT INTO public.tasks (title, description, state, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    cur.execute(
        query, 
        (
            task.title, 
            task.description, 
            task.state.value, 
            datetime.now().isoformat(), 
            datetime.now().isoformat()
        )
    )
    data = cur.fetchone()
    return data

def query_update_task_by_id(cur, id: int, task: TaskUpdate):
    query = """
    UPDATE public.tasks 
    SET title = %s, 
        description = %s, 
        state = %s, 
        updated_at = %s
    WHERE 
        id = %s
    RETURNING *
    """
    cur.execute(
        query, 
        (
            task.title, 
            task.description, 
            task.state.value, 
            datetime.now().isoformat(),
            id
        )
    )
    data = cur.fetchone()
    return data

def query_delete_task_by_id(cur, id: int):
    query = """
    DELETE FROM public.tasks 
    WHERE id = %s
    RETURNING id
    """
    cur.execute(query, (id, ))
    return cur.fetchone()