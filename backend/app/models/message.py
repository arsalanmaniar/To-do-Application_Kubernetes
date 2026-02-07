from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from app.models.conversation import Conversation  # Import Conversation model for relationship


class MessageBase(SQLModel):
    conversation_id: uuid.UUID = Field(foreign_key="conversation.id", nullable=False)
    sender: str = Field(sa_column_kwargs={"server_default": "user"})  # 'user' or 'ai'
    content: str = Field(min_length=1, max_length=10000)


class Message(MessageBase, table=True):
    """
    Message model representing a message in a conversation
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to conversation
    conversation: Optional[Conversation] = Relationship(back_populates="messages")


class MessageCreate(MessageBase):
    """
    Schema for creating a new message
    """
    conversation_id: uuid.UUID
    sender: str  # 'user' or 'ai'
    content: str


class MessageRead(MessageBase):
    """
    Schema for reading a message
    """
    id: uuid.UUID
    created_at: datetime


class MessageUpdate(SQLModel):
    """
    Schema for updating a message (content only)
    """
    content: Optional[str] = Field(default=None, min_length=1, max_length=10000)