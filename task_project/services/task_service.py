from schemas.task_schema import Task, TaskWithID

db: dict[int, TaskWithID] = {}
next_id: int = 1

def get_all():
    return list(db.values())

def create(data: Task):
    global next_id
    
    saved_task = TaskWithID(
        id=next_id, 
        title=data.title, 
        description=data.description, 
        completed=data.completed
    )
    
    db[next_id] = saved_task
    next_id += 1
    
    return saved_task

def update(id: int, data: Task):
    if id not in db:
        return None  
        
    changed_task = TaskWithID(
        id=id, 
        title=data.title, 
        description=data.description, 
        completed=data.completed
    )
    
    db[id] = changed_task
    return changed_task

def delete(id: int):
    if id in db:
        del db[id]
        return True
    return False