from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate

# Our in-memory database
task_db: dict[int, TaskResponse] = {}
current_id: int = 1

def get_all_tasks() -> list[TaskResponse]:
    """Return a list of all tasks in the database."""
    return list(task_db.values())

def create_task(task_in: TaskCreate) -> TaskResponse:
    """Create a new task and save it to the database."""
    global current_id
    new_task = TaskResponse(
        id=current_id,
        title=task_in.title,
        description=task_in.description,
        completed=False
    )
    task_db[current_id] = new_task
    current_id += 1
    return new_task

def update_task(task_id: int, task_in: TaskCreate) -> TaskResponse | None:
    """Fully replace an existing task."""
    if task_id not in task_db:
        return None
    
    # Keep the same ID, but overwrite everything else
    updated_task = TaskResponse(
        id=task_id,
        title=task_in.title,
        description=task_in.description,
        completed=task_db[task_id].completed # Keep existing completion status
    )
    task_db[task_id] = updated_task
    return updated_task

def patch_task(task_id: int, task_in: TaskUpdate) -> TaskResponse | None:
    """Partially update a task without overwriting unchanged fields."""
    if task_id not in task_db:
        return None
        
    existing_task = task_db[task_id]
    
    # Extract only the fields the user actually sent
    update_data = task_in.model_dump(exclude_unset=True) 
    
    # Create a copy of the existing task with the new changes applied
    updated_task = existing_task.model_copy(update=update_data)
    
    task_db[task_id] = updated_task
    return updated_task

def delete_task(task_id: int) -> bool:
    """Delete a task from the database. Returns True if successful."""
    if task_id in task_db:
        del task_db[task_id]
        return True
    return False