from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import Optional
from app.services.message_service import MessageService
from app.schemas.message import (
    MessageCreate, MessageRead, MessageUpdate
)
from app.core.dependencies import get_current_user_id, get_db_session
from app.core.logging import logger
from datetime import datetime
import uuid

router = APIRouter()


@router.post("/messages", response_model=MessageRead, status_code=201)
def create_message(
    message_data: MessageCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new message in a conversation
    """
    try:
        message = MessageService.create_message(
            session=session,
            message_data=message_data,
            user_id=current_user_id
        )

        return MessageRead(
            id=message.id,
            conversation_id=message.conversation_id,
            sender=message.sender,
            content=message.content,
            created_at=message.created_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating message for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/messages/{message_id}", response_model=MessageRead)
def get_message(
    message_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve a specific message by ID
    """
    try:
        message = MessageService.get_message_by_id(
            session=session,
            message_id=message_id,
            user_id=current_user_id
        )

        return MessageRead(
            id=message.id,
            conversation_id=message.conversation_id,
            sender=message.sender,
            content=message.content,
            created_at=message.created_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting message {message_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/messages/{message_id}", response_model=MessageRead)
def update_message(
    message_id: str,
    message_data: MessageUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific message completely
    """
    try:
        message = MessageService.update_message(
            session=session,
            message_id=message_id,
            message_data=message_data,
            user_id=current_user_id
        )

        return MessageRead(
            id=message.id,
            conversation_id=message.conversation_id,
            sender=message.sender,
            content=message.content,
            created_at=message.created_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating message {message_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/messages/{message_id}", response_model=MessageRead)
def patch_message(
    message_id: str,
    message_data: MessageUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Partially update a specific message
    """
    try:
        message = MessageService.update_message(
            session=session,
            message_id=message_id,
            message_data=message_data,
            user_id=current_user_id
        )

        return MessageRead(
            id=message.id,
            conversation_id=message.conversation_id,
            sender=message.sender,
            content=message.content,
            created_at=message.created_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error patching message {message_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/messages/{message_id}", status_code=204)
def delete_message(
    message_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific message
    """
    try:
        MessageService.delete_message(
            session=session,
            message_id=message_id,
            user_id=current_user_id
        )
        return
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting message {message_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")