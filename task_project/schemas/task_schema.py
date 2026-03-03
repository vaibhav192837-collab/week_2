from pydantic import BaseModel

# What the user types in
class Task(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

# What we send back to them
class TaskWithID(Task):
    id: int