# 1. Base Image
FROM python:3.14-slim

# 2. Working Directory
WORKDIR /app

# 3. Install uv
RUN pip install uv

# 4. Dependencies: Copy your uv dependency file
COPY pyproject.toml .

# 5. Install using uv
RUN uv pip install --system -r pyproject.toml

# 6. Copy Code (Copies files from your host machine  to  container image.)
COPY . .

# 7. Expose Port (Documents the port the container listens on. Does not actually publish the port.)
EXPOSE 8000

# 8. Start Command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]