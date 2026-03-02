from fastapi import APIRouter, HTTPException, Path, status
from schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from services import task_service

# Create the router
router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=list[TaskResponse])
def get_tasks() -> list[TaskResponse]:
    """GET /tasks: Returns a list of all tasks."""
    return task_service.get_all_tasks()

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate) -> TaskResponse:
    """POST /tasks: Creates a new task."""
    return task_service.create_task(task)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task: TaskCreate, 
    task_id: int = Path(..., gt=0, description="The ID of the task to completely replace")
) -> TaskResponse:
    """PUT /tasks/{id}: Fully updates an existing task. Requires all fields."""
    updated = task_service.update_task(task_id, task)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )
    return updated

@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(
    task: TaskUpdate, 
    task_id: int = Path(..., gt=0, description="The ID of the task to partially update")
) -> TaskResponse:
    """PATCH /tasks/{id}: Partially updates an existing task. Only provided fields are updated."""
    updated = task_service.patch_task(task_id, task)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int = Path(..., gt=0, description="The ID of the task to delete")
) -> None:
    """DELETE /tasks/{id}: Removes a task from the database."""
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )