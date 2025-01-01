from typing import List, Tuple

def query_select_tasks( cur ) -> List[Tuple]:
    query = """
    SELECT 
        id, title, description, state, created_at, updated_at
    FROM
        public.tasks
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
    