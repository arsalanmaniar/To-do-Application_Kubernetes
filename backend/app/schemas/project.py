from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: str


class ProjectCreate(ProjectBase):
    name: str
    description: Optional[str] = None
    owner_id: str


class ProjectRead(ProjectBase):
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectListResponse(BaseModel):
    projects: list[ProjectRead]
    total: int
    limit: int
    offset: int