from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class ConversationBase(BaseModel):
    title: str
    owner_id: str


class ConversationCreate(ConversationBase):
    title: str
    owner_id: str


class ConversationRead(ConversationBase):
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class ConversationUpdate(BaseModel):
    title: Optional[str] = None


class ConversationListResponse(BaseModel):
    conversations: list[ConversationRead]
    total: int
    limit: int
    offset: int