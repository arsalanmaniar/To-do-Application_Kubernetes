from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from app.models.user import User
from app.models.task import Task  # Import Task model for relationship


class CalendarEventBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)
    start_time: datetime
    end_time: datetime
    all_day: bool = Field(default=False)
    owner_id: str = Field(foreign_key="user.id", nullable=False)
    task_id: Optional[uuid.UUID] = Field(foreign_key="task.id", nullable=True)


class CalendarEvent(CalendarEventBase, table=True):
    """
    CalendarEvent model representing a calendar event that can be linked to a task
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    owner: Optional[User] = Relationship(back_populates="calendar_events")
    task: Optional[Task] = Relationship(back_populates="calendar_events")


class CalendarEventCreate(CalendarEventBase):
    """
    Schema for creating a new calendar event
    """
    title: str
    start_time: datetime
    end_time: datetime
    owner_id: str


class CalendarEventRead(CalendarEventBase):
    """
    Schema for reading a calendar event
    """
    id: uuid.UUID
    owner_id: str
    task_id: Optional[uuid.UUID]
    created_at: datetime
    updated_at: datetime


class CalendarEventUpdate(SQLModel):
    """
    Schema for updating a calendar event (all fields optional for partial updates)
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=2000)
    start_time: Optional[datetime] = Field(default=None)
    end_time: Optional[datetime] = Field(default=None)
    all_day: Optional[bool] = Field(default=None)