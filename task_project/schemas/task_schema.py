from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    """Schema for creating a new task."""
    title: str = Field(..., min_length=1, max_length=100, description="The title of the task")
    description: str | None = Field(default=None, description="Optional details about the task")

class TaskResponse(TaskCreate):
    """Schema for returning a task to the user."""
    id: int
    completed: bool = False

class TaskUpdate(BaseModel):
    """Schema for partially updating an existing task."""
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None)
    completed: bool | None = Field(default=None)
    