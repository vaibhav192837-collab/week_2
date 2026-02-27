from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    """Schema for creating or updating a task."""
    title: str = Field(..., min_length=1, max_length=100, description="Title of the task")
    description: str | None = Field(default=None, description="Optional details")
    completed: bool = Field(default=False, description="Task status")

class TaskResponse(TaskCreate):
    """Schema for returning a task, includes the ID."""
    id: int
    
class TaskUpdate(BaseModel):
    """Schema for partially updating a task."""
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None)
    completed: bool | None = Field(default=None)