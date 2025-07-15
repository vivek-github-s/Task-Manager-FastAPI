from fastapi import FastAPI
from app.api import user, project, task

app = FastAPI(title="Task Manager API")

# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(project.router, prefix="/projects", tags=["Projects"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"msg": "Welcome to Task Manager API"}