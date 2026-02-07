from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class MessageBase(BaseModel):
    conversation_id: uuid.UUID
    sender: str  # 'user' or 'ai'
    content: str


class MessageCreate(MessageBase):
    conversation_id: uuid.UUID
    sender: str  # 'user' or 'ai'
    content: str


class MessageRead(MessageBase):
    id: uuid.UUID
    created_at: datetime


class MessageUpdate(BaseModel):
    content: Optional[str] = None


class MessageListResponse(BaseModel):
    messages: list[MessageRead]
    total: int
    limit: int
    offset: int