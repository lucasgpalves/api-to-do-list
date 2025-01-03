from typing import List, Tuple, Optional
from .models import Task, TaskCreate, TaskUpdate
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session

def query_select_tasks(session: Session) -> List[Tuple]:
    query = select(Task).order_by(Task.id)
    data = session.execute(query).scalars().all()
    return data

def query_select_task_by_id(session: Session, id: int) -> Optional[Tuple]:
    data = session.query(Task).filter(Task.id == id).first()
    return data

def query_insert_task(session: Session, task: TaskCreate) -> tuple:
    new_task = Task(
        title=task.title,
        description=task.description,
        state=task.state.value,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

def query_update_task_by_id(session: Session, id: int, task: TaskUpdate):
    task_to_update = session.query(Task).filter(Task.id == id).first()

    if task_to_update:
        task_to_update.title = task.title
        task_to_update.description = task.description
        task_to_update.state = task.state.value
        task_to_update.updated_at = datetime.now()

        session.commit()

        return task_to_update
    else:
        return None

def query_delete_task_by_id(session: Session, id: int):
    task_to_delete = session.query(Task).filter(Task.id == id).first()

    if task_to_delete:
        session.delete(task_to_delete)
        session.commit()

        return 1
    
    return None