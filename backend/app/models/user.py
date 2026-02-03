from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class UserBase(SQLModel):
    id: str = Field(primary_key=True)
    email: str = Field(nullable=False)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    """
    User model representing a registered user
    """
    created_at: datetime = Field(default_factory=datetime.utcnow)
    hashed_password: str = Field()

    # Relationship to tasks (using string reference to avoid circular imports)
    tasks: List["Task"] = Relationship(back_populates="owner")

    # Relationship to projects (using string reference to avoid circular imports)
    projects: List["Project"] = Relationship(back_populates="owner")

    # Relationship to teams (using string reference to avoid circular imports)
    teams: List["Team"] = Relationship(back_populates="owner")

    # Relationship to calendar events (using string reference to avoid circular imports)
    calendar_events: List["CalendarEvent"] = Relationship(back_populates="owner")

    # Relationship to conversations (using string reference to avoid circular imports)
    conversations: List["Conversation"] = Relationship(back_populates="owner")

    # Relationship to team memberships (using string reference to avoid circular imports)
    team_memberships: List["TeamMembership"] = Relationship(back_populates="user")


class UserRead(UserBase):
    """
    Schema for reading user information
    """
    created_at: datetime