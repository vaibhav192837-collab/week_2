# Simple Modular Task Manager API

A clean, foundational REST API built with FastAPI. This project demonstrates enterprise-grade software architecture using the "Separation of Concerns" principle, keeping web traffic, data validation, and business logic completely isolated from one another.

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Data Validation:** Pydantic
* **Server:** Uvicorn
* **Package Manager:** uv

## 📂 Project Architecture

This application uses a strict 3-tier layered architecture:

* **`/schemas` (Data Validation):** Contains Pydantic models (`Task` and `TaskWithID`) that act as bouncers, ensuring only strictly typed JSON data enters and exits the API.
* **`/routers` (Interface Layer):** Contains the FastAPI `APIRouter` endpoints. This layer only handles HTTP web traffic (GET, POST, PUT, DELETE) and error handling (404s).
* **`/services` (Business Logic):** Contains the core Python logic and the in-memory dictionary database. It knows nothing about the internet or HTTP requests.

## 🚀 How to Run the Server

1. Make sure you are in the root `task_project` directory.
2. Run the following command in your terminal to start the Uvicorn server:
   ```bash
   uv run uvicorn main:app --reload