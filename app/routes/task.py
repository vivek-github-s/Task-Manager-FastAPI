from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.task import Task
from app.schemas.task import TaskCreate

async def create_task(db: AsyncSession, task_in: TaskCreate) -> Task:
    task = Task(**task_in.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_task(db: AsyncSession, task_id: int) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

async def list_tasks(db: AsyncSession) -> list[Task]:
    result = await db.execute(select(Task))
    return result.scalars().all()