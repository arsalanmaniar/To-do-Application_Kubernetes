from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid
from app.models.user import User  # Import User model for relationship


class ConversationBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    owner_id: str = Field(foreign_key="user.id", nullable=False)


class Conversation(ConversationBase, table=True):
    """
    Conversation model representing a conversation between user and AI
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user (owner)
    owner: Optional[User] = Relationship(back_populates="conversations")

    # Relationship to messages
    messages: List["Message"] = Relationship(back_populates="conversation")


class ConversationCreate(ConversationBase):
    """
    Schema for creating a new conversation
    """
    title: str
    owner_id: str


class ConversationRead(ConversationBase):
    """
    Schema for reading a conversation
    """
    id: uuid.UUID
    owner_id: str
    created_at: datetime
    updated_at: datetime


class ConversationUpdate(SQLModel):
    """
    Schema for updating a conversation (title only)
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)