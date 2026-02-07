from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import Optional
from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.schemas.conversation import (
    ConversationCreate, ConversationRead, ConversationUpdate, ConversationListResponse
)
from app.schemas.message import MessageListResponse
from app.core.dependencies import get_current_user_id, get_db_session
from app.core.logging import logger
from datetime import datetime
import uuid

router = APIRouter()


@router.get("/conversations", response_model=ConversationListResponse)
def get_conversations(
    current_user_id: str = Depends(get_current_user_id),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve all conversations for the specified user
    """
    try:
        conversations, total = ConversationService.get_conversations_by_user(
            session=session,
            owner_id=current_user_id,
            limit=limit,
            offset=offset
        )

        conversation_responses = []
        for conversation in conversations:
            conversation_response = ConversationRead(
                id=conversation.id,
                title=conversation.title,
                owner_id=conversation.owner_id,
                created_at=conversation.created_at,
                updated_at=conversation.updated_at
            )
            conversation_responses.append(conversation_response)

        return ConversationListResponse(
            conversations=conversation_responses,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        logger.error(f"Error getting conversations for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/conversations", response_model=ConversationRead, status_code=201)
def create_conversation(
    conversation_data: ConversationCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new conversation for the current user
    """
    try:
        conversation = ConversationService.create_conversation(
            session=session,
            conversation_data=conversation_data,
            owner_id=current_user_id
        )

        return ConversationRead(
            id=conversation.id,
            title=conversation.title,
            owner_id=conversation.owner_id,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating conversation for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/conversations/{conversation_id}", response_model=ConversationRead)
def get_conversation(
    conversation_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve a specific conversation by ID
    """
    try:
        conversation = ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=conversation_id,
            owner_id=current_user_id
        )

        return ConversationRead(
            id=conversation.id,
            title=conversation.title,
            owner_id=conversation.owner_id,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting conversation {conversation_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/conversations/{conversation_id}", response_model=ConversationRead)
def update_conversation(
    conversation_id: str,
    conversation_data: ConversationUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific conversation completely
    """
    try:
        conversation = ConversationService.update_conversation(
            session=session,
            conversation_id=conversation_id,
            conversation_data=conversation_data,
            owner_id=current_user_id
        )

        return ConversationRead(
            id=conversation.id,
            title=conversation.title,
            owner_id=conversation.owner_id,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating conversation {conversation_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/conversations/{conversation_id}", response_model=ConversationRead)
def patch_conversation(
    conversation_id: str,
    conversation_data: ConversationUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Partially update a specific conversation
    """
    try:
        conversation = ConversationService.update_conversation(
            session=session,
            conversation_id=conversation_id,
            conversation_data=conversation_data,
            owner_id=current_user_id
        )

        return ConversationRead(
            id=conversation.id,
            title=conversation.title,
            owner_id=conversation.owner_id,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error patching conversation {conversation_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/conversations/{conversation_id}", status_code=204)
def delete_conversation(
    conversation_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific conversation
    """
    try:
        ConversationService.delete_conversation(
            session=session,
            conversation_id=conversation_id,
            owner_id=current_user_id
        )
        return
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting conversation {conversation_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/conversations/{conversation_id}/messages", response_model=MessageListResponse)
def get_conversation_messages(
    conversation_id: str,
    current_user_id: str = Depends(get_current_user_id),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve all messages in a specific conversation for the user
    """
    try:
        messages, total = MessageService.get_messages_by_conversation(
            session=session,
            conversation_id=conversation_id,
            user_id=current_user_id,
            limit=limit,
            offset=offset
        )

        message_responses = []
        for message in messages:
            message_response = {
                "id": message.id,
                "conversation_id": message.conversation_id,
                "sender": message.sender,
                "content": message.content,
                "created_at": message.created_at
            }
            message_responses.append(message_response)

        return MessageListResponse(
            messages=message_responses,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        logger.error(f"Error getting messages for conversation {conversation_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")