from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid
from app.models.user import User  # Import User model for relationship


class TeamBase(SQLModel):
    name: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)
    owner_id: str = Field(foreign_key="user.id", nullable=False)


class Team(TeamBase, table=True):
    """
    Team model representing a collaborative team of users
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user (owner)
    owner: Optional[User] = Relationship(back_populates="teams")

    # Relationship to team memberships
    memberships: List["TeamMembership"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    """
    Schema for creating a new team
    """
    pass


class TeamRead(TeamBase):
    """
    Schema for reading a team
    """
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class TeamUpdate(SQLModel):
    """
    Schema for updating a team (all fields optional for partial updates)
    """
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)