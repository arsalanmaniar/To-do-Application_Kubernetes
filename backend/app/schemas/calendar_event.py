from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class CalendarEventBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    all_day: bool = False
    owner_id: str
    task_id: Optional[uuid.UUID] = None


class CalendarEventCreate(CalendarEventBase):
    title: str
    start_time: datetime
    end_time: datetime
    owner_id: str


class CalendarEventRead(CalendarEventBase):
    id: uuid.UUID
    owner_id: str
    task_id: Optional[uuid.UUID] = None
    created_at: datetime
    updated_at: datetime


class CalendarEventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    all_day: Optional[bool] = None


class CalendarEventListResponse(BaseModel):
    events: list[CalendarEventRead]
    total: int
    limit: int
    offset: int