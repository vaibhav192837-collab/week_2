from fastapi import FastAPI
from routers.task_router import router as task_router

app = FastAPI(title="Task Manager API")

# Plug in the modular routes
app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Modular Task Manager API!"}