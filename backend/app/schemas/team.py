from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class TeamBase(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: str


class TeamCreate(TeamBase):
    name: str
    description: Optional[str] = None
    owner_id: str


class TeamRead(TeamBase):
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class TeamUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class TeamListResponse(BaseModel):
    teams: list[TeamRead]
    total: int
    limit: int
    offset: int