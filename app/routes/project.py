from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.project import Project
from app.schemas.project import ProjectCreate
from app.db.models.user import User
async def create_project(db: AsyncSession, project_in: ProjectCreate,current_user: User) -> Project:
    project = Project(**project_in.dict(),owner_id=current_user.id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project

async def get_project(db: AsyncSession, project_id: int) -> Project | None:
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalars().first()

async def list_projects(db: AsyncSession) -> list[Project]:
    result = await db.execute(select(Project))
    return result.scalars().all()