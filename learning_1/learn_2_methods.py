from fastapi import FastAPI

app = FastAPI()

# A simple Python list acting as our temporary "database"
fake_tasks = ["Setup uv", "Learn FastAPI routesss"]

# 1. GET Method: Read data
@app.get("/tasks")
def get_tasks():
    """Returns the current list of tasks."""
    return {"tasks": fake_tasks}

# 2. POST Method: Create data
@app.post("/tasks")
def create_task(new_task: str):
    """Adds a new task to the list."""
    fake_tasks.append(new_task)
    return {"message": f"Successfully added '{new_task}'!"}

# 3. PUT Method: Update data
@app.put("/tasks/{task_index}")
def update_task(task_index: int, updated_task_name: str):
    """Updates an existing task based on its index in the list."""
    # For this trial, we use the list index (0, 1, 2) as the task ID
    fake_tasks[task_index] = updated_task_name
    return {"message": f"Task at index {task_index} updated to '{updated_task_name}'"}

# 4. DELETE Method: Remove data
@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    """Removes a task from the list based on its index."""
    removed_task = fake_tasks.pop(task_index)
    return {"message": f"Deleted '{removed_task}'"}