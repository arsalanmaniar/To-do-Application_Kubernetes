from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from app.models.user import User
from app.models.team import Team  # Import Team model for relationship


class TeamMembershipBase(SQLModel):
    team_id: uuid.UUID = Field(foreign_key="team.id", nullable=False)
    user_id: str = Field(foreign_key="user.id", nullable=False)
    role: str = Field(default="member", sa_column_kwargs={"server_default": "member"})  # 'member' or 'admin'


class TeamMembership(TeamMembershipBase, table=True):
    """
    TeamMembership model representing the relationship between users and teams
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    joined_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    team: Optional[Team] = Relationship(back_populates="memberships")
    user: Optional[User] = Relationship(back_populates="team_memberships")


class TeamMembershipCreate(TeamMembershipBase):
    """
    Schema for creating a new team membership
    """
    team_id: uuid.UUID
    user_id: str
    role: str = "member"  # Default role is member


class TeamMembershipRead(TeamMembershipBase):
    """
    Schema for reading a team membership
    """
    id: uuid.UUID
    joined_at: datetime


class TeamMembershipUpdate(SQLModel):
    """
    Schema for updating a team membership (role only)
    """
    role: Optional[str] = Field(default=None)  # Can be 'member' or 'admin'