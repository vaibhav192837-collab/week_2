from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[TaskResponse])
def read_tasks():
    """GET /tasks: Returns all tasks."""
    return task_service.get_all_tasks()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """POST /tasks: Creates a new task."""
    return task_service.create_task(task)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    """PUT /tasks/{id}: Updates an existing task."""
    updated = task_service.update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """DELETE /tasks/{id}: Removes a task."""
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    
@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task: TaskUpdate):
    """PATCH /tasks/{id}: Partially updates a task."""
    updated = task_service.patch_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return updated