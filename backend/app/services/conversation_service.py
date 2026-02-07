from sqlmodel import Session, select
from typing import List, Optional
from app.models.conversation import Conversation, ConversationCreate, ConversationUpdate
from app.core.exceptions import ConversationNotFoundException, UnauthorizedAccessException
from app.core.logging import logger


class ConversationService:
    """
    Service class for handling conversation-related operations
    """

    @staticmethod
    def create_conversation(session: Session, conversation_data: ConversationCreate, owner_id: str) -> Conversation:
        """
        Create a new conversation for a user
        """
        conversation = Conversation(
            title=conversation_data.title,
            owner_id=owner_id
        )
        session.add(conversation)
        session.commit()
        session.refresh(conversation)

        logger.info(f"Created conversation {conversation.id} for user {owner_id}")
        return conversation

    @staticmethod
    def get_conversation_by_id(session: Session, conversation_id: str, owner_id: str) -> Conversation:
        """
        Get a specific conversation by ID for a specific user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(conversation_id) if isinstance(conversation_id, str) and conversation_id else conversation_id
        conversation = session.get(Conversation, uuid_obj)
        if not conversation:
            raise ConversationNotFoundException(conversation_id)

        if conversation.owner_id != owner_id:
            raise UnauthorizedAccessException()

        return conversation

    @staticmethod
    def get_conversations_by_user(
        session: Session,
        owner_id: str,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[List[Conversation], int]:
        """
        Get all conversations for a specific user
        """
        query = select(Conversation).where(Conversation.owner_id == owner_id)

        # Get total count for pagination
        count_query = select(Conversation).where(Conversation.owner_id == owner_id)
        total = len(session.exec(count_query).all())

        # Apply pagination
        query = query.offset(offset).limit(limit)
        conversations = session.exec(query).all()

        return conversations, total

    @staticmethod
    def update_conversation(session: Session, conversation_id: str, conversation_data: ConversationUpdate, owner_id: str) -> Conversation:
        """
        Update a specific conversation for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(conversation_id) if isinstance(conversation_id, str) and conversation_id else conversation_id
        conversation = session.get(Conversation, uuid_obj)
        if not conversation:
            raise ConversationNotFoundException(conversation_id)

        if conversation.owner_id != owner_id:
            raise UnauthorizedAccessException()

        # Update conversation fields
        for field, value in conversation_data.dict(exclude_unset=True).items():
            setattr(conversation, field, value)

        conversation.updated_at = type(conversation.updated_at).utcnow()  # Update timestamp

        session.add(conversation)
        session.commit()
        session.refresh(conversation)

        logger.info(f"Updated conversation {conversation.id} for user {owner_id}")
        return conversation

    @staticmethod
    def delete_conversation(session: Session, conversation_id: str, owner_id: str) -> bool:
        """
        Delete a specific conversation for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(conversation_id) if isinstance(conversation_id, str) and conversation_id else conversation_id
        conversation = session.get(Conversation, uuid_obj)
        if not conversation:
            raise ConversationNotFoundException(conversation_id)

        if conversation.owner_id != owner_id:
            raise UnauthorizedAccessException()

        session.delete(conversation)
        session.commit()

        logger.info(f"Deleted conversation {conversation.id} for user {owner_id}")
        return True