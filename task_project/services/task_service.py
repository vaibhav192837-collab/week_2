from typing import Dict, List
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate

# In-memory storage using a dictionary for fast ID lookups
task_db: Dict[int, TaskResponse] = {}
current_id: int = 1

def get_all_tasks() -> List[TaskResponse]:
    """Fetch all tasks from the database."""
    return list(task_db.values())

def create_task(task_in: TaskCreate) -> TaskResponse:
    """Create a new task and assign it an ID."""
    global current_id
    new_task = TaskResponse(id=current_id, **task_in.model_dump())
    task_db[current_id] = new_task
    current_id += 1
    return new_task

def update_task(task_id: int, task_in: TaskCreate) -> TaskResponse | None:
    """Update an existing task. Returns None if not found."""
    if task_id not in task_db:
        return None
    updated_task = TaskResponse(id=task_id, **task_in.model_dump())
    task_db[task_id] = updated_task
    return updated_task

def delete_task(task_id: int) -> bool:
    """Delete a task. Returns True if successful, False if not found."""
    if task_id in task_db:
        del task_db[task_id]
        return True
    return False

def patch_task(task_id: int, task_in: TaskUpdate) -> TaskResponse | None:
    """Partially update a task without overwriting everything."""
    if task_id not in task_db:
        return None

    existing_task = task_db[task_id]
    update_data = task_in.model_dump(exclude_unset=True) 
    updated_task = existing_task.model_copy(update=update_data)

    task_db[task_id] = updated_task
    return updated_task