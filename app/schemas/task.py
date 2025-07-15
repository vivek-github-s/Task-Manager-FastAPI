from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False
    due_date: datetime | None = None

class TaskCreate(TaskBase):
    project_id: int
    created_by_id: int

class TaskOut(TaskBase):
    id: int
    project_id: int
    created_by_id: int
    created_at: datetime

    class Config:
        orm_mode = True