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