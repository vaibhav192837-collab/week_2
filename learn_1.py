from fastapi import FastAPI

# 1. Create the API application
app = FastAPI()

# 2. Tell the app to listen for a GET request at the root URL ("/")
@app.get("/")
def say_hello():
    # 3. Return some data
    return {"message": "Hello, Week 2! hi"}