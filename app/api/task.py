from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.sessions import get_db
from app.schemas.task import TaskCreate, TaskOut
from app.routes import task as crud_task
from app.db.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task(task_in: TaskCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user),):
    return await crud_task.create_task(db, task_in)

@router.get("/", response_model=list[TaskOut])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await crud_task.list_tasks(db)