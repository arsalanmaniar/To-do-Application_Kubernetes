from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import Optional
from app.services.project_service import ProjectService
from app.schemas.project import (
    ProjectCreate, ProjectRead, ProjectUpdate, ProjectListResponse
)
from app.core.dependencies import get_current_user_id, get_db_session
from app.core.logging import logger
from datetime import datetime
import uuid

router = APIRouter()


@router.get("/projects", response_model=ProjectListResponse)
def get_projects(
    current_user_id: str = Depends(get_current_user_id),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve all projects for the specified user
    """
    try:
        projects, total = ProjectService.get_projects_by_user(
            session=session,
            owner_id=current_user_id,
            limit=limit,
            offset=offset
        )

        project_responses = []
        for project in projects:
            project_response = ProjectRead(
                id=project.id,
                name=project.name,
                description=project.description,
                owner_id=project.owner_id,
                created_at=project.created_at,
                updated_at=project.updated_at
            )
            project_responses.append(project_response)

        return ProjectListResponse(
            projects=project_responses,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        logger.error(f"Error getting projects for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/projects", response_model=ProjectRead, status_code=201)
def create_project(
    project_data: ProjectCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new project for the current user
    """
    try:
        project = ProjectService.create_project(
            session=session,
            project_data=project_data,
            owner_id=current_user_id
        )

        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            created_at=project.created_at,
            updated_at=project.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating project for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/projects/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve a specific project by ID
    """
    try:
        project = ProjectService.get_project_by_id(
            session=session,
            project_id=project_id,
            owner_id=current_user_id
        )

        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            created_at=project.created_at,
            updated_at=project.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting project {project_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/projects/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: str,
    project_data: ProjectUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific project completely
    """
    try:
        project = ProjectService.update_project(
            session=session,
            project_id=project_id,
            project_data=project_data,
            owner_id=current_user_id
        )

        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            created_at=project.created_at,
            updated_at=project.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating project {project_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/projects/{project_id}", response_model=ProjectRead)
def patch_project(
    project_id: str,
    project_data: ProjectUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Partially update a specific project
    """
    try:
        project = ProjectService.update_project(
            session=session,
            project_id=project_id,
            project_data=project_data,
            owner_id=current_user_id
        )

        return ProjectRead(
            id=project.id,
            name=project.name,
            description=project.description,
            owner_id=project.owner_id,
            created_at=project.created_at,
            updated_at=project.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error patching project {project_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/projects/{project_id}", status_code=204)
def delete_project(
    project_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific project
    """
    try:
        ProjectService.delete_project(
            session=session,
            project_id=project_id,
            owner_id=current_user_id
        )
        return
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting project {project_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")