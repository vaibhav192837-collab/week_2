from fastapi import APIRouter, HTTPException
from schemas.task_schema import Task, TaskWithID
from services import task_service

router = APIRouter(prefix="/tasks")

@router.get("", response_model=list[TaskWithID])
def list_tasks():
    return task_service.get_all()

@router.post("", response_model=TaskWithID)
def add_task(data: Task):
    return task_service.create(data)

@router.put("/{id}", response_model=TaskWithID)
def change_task(id: int, data: Task):
    changed = task_service.update(id, data)
    
    if not changed:
        raise HTTPException(status_code=404, detail="Task not found")
        
    return changed

@router.delete("/{id}")
def remove_task(id: int):
    is_deleted = task_service.delete(id)
    
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Task not found")
        
    return {"message": "Task deleted successfully!"}