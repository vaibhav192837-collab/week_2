from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.task_router import router as task_router

app = FastAPI(title="Task Manager API")

# ADD THIS BLOCK to allow your frontend to talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any frontend to connect
    allow_credentials=True,
    allow_methods=["*"], # Allows GET, POST, PUT, DELETE
    allow_headers=["*"],
)

app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Modular Task Manager API!"}