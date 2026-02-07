from sqlmodel import Session, select
from typing import List, Optional
from app.models.project import Project, ProjectCreate, ProjectUpdate
from app.core.exceptions import ProjectNotFoundException, UnauthorizedAccessException
from app.core.logging import logger


class ProjectService:
    """
    Service class for handling project-related operations
    """

    @staticmethod
    def create_project(session: Session, project_data: ProjectCreate, owner_id: str) -> Project:
        """
        Create a new project for a user
        """
        project = Project(
            name=project_data.name,
            description=project_data.description,
            owner_id=owner_id
        )
        session.add(project)
        session.commit()
        session.refresh(project)

        logger.info(f"Created project {project.id} for user {owner_id}")
        return project

    @staticmethod
    def get_project_by_id(session: Session, project_id: str, owner_id: str) -> Project:
        """
        Get a specific project by ID for a specific user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(project_id) if isinstance(project_id, str) and project_id else project_id
        project = session.get(Project, uuid_obj)
        if not project:
            raise ProjectNotFoundException(project_id)

        if project.owner_id != owner_id:
            raise UnauthorizedAccessException()

        return project

    @staticmethod
    def get_projects_by_user(
        session: Session,
        owner_id: str,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[List[Project], int]:
        """
        Get all projects for a specific user
        """
        query = select(Project).where(Project.owner_id == owner_id)

        # Get total count for pagination
        count_query = select(Project).where(Project.owner_id == owner_id)
        total = len(session.exec(count_query).all())

        # Apply pagination
        query = query.offset(offset).limit(limit)
        projects = session.exec(query).all()

        return projects, total

    @staticmethod
    def update_project(session: Session, project_id: str, project_data: ProjectUpdate, owner_id: str) -> Project:
        """
        Update a specific project for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(project_id) if isinstance(project_id, str) and project_id else project_id
        project = session.get(Project, uuid_obj)
        if not project:
            raise ProjectNotFoundException(project_id)

        if project.owner_id != owner_id:
            raise UnauthorizedAccessException()

        # Update project fields
        for field, value in project_data.dict(exclude_unset=True).items():
            setattr(project, field, value)

        project.updated_at = type(project.updated_at).utcnow()  # Update timestamp

        session.add(project)
        session.commit()
        session.refresh(project)

        logger.info(f"Updated project {project.id} for user {owner_id}")
        return project

    @staticmethod
    def delete_project(session: Session, project_id: str, owner_id: str) -> bool:
        """
        Delete a specific project for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(project_id) if isinstance(project_id, str) and project_id else project_id
        project = session.get(Project, uuid_obj)
        if not project:
            raise ProjectNotFoundException(project_id)

        if project.owner_id != owner_id:
            raise UnauthorizedAccessException()

        session.delete(project)
        session.commit()

        logger.info(f"Deleted project {project.id} for user {owner_id}")
        return True