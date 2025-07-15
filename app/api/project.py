from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.sessions import get_db
from app.schemas.project import ProjectCreate, ProjectOut
from app.routes import project as crud_project
from app.db.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=ProjectOut)
async def create_project(
    project_in: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await crud_project.create_project(db, project_in, current_user)

@router.get("/", response_model=list[ProjectOut])
async def get_projects(db: AsyncSession = Depends(get_db)):
    return await crud_project.list_projects(db)
