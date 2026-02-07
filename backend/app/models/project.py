from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from app.models.user import User  # Import User model for relationship


class ProjectBase(SQLModel):
    name: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)
    owner_id: str = Field(foreign_key="user.id", nullable=False)


class Project(ProjectBase, table=True):
    """
    Project model representing a user's project that can contain tasks
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user (owner)
    owner: Optional[User] = Relationship(back_populates="projects")


class ProjectCreate(ProjectBase):
    """
    Schema for creating a new project
    """
    pass


class ProjectRead(ProjectBase):
    """
    Schema for reading a project
    """
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(SQLModel):
    """
    Schema for updating a project (all fields optional for partial updates)
    """
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)