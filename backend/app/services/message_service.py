from sqlmodel import Session, select
from typing import List, Optional
from app.models.message import Message, MessageCreate, MessageUpdate
from app.core.exceptions import MessageNotFoundException, UnauthorizedAccessException, ConversationNotFoundException
from app.core.logging import logger
from app.services.conversation_service import ConversationService


class MessageService:
    """
    Service class for handling message-related operations
    """

    @staticmethod
    def create_message(session: Session, message_data: MessageCreate, user_id: str) -> Message:
        """
        Create a new message in a conversation
        """
        # Verify the user has access to the conversation
        ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=str(message_data.conversation_id),
            owner_id=user_id
        )

        message = Message(
            conversation_id=message_data.conversation_id,
            sender=message_data.sender,
            content=message_data.content
        )
        session.add(message)
        session.commit()
        session.refresh(message)

        logger.info(f"Created message {message.id} in conversation {message.conversation_id}")
        return message

    @staticmethod
    def get_message_by_id(session: Session, message_id: str, user_id: str) -> Message:
        """
        Get a specific message by ID for a specific user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(message_id) if isinstance(message_id, str) and message_id else message_id
        message = session.get(Message, uuid_obj)
        if not message:
            raise MessageNotFoundException(message_id)

        # Verify the user has access to the conversation that contains this message
        ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=str(message.conversation_id),
            owner_id=user_id
        )

        return message

    @staticmethod
    def get_messages_by_conversation(
        session: Session,
        conversation_id: str,
        user_id: str,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[List[Message], int]:
        """
        Get all messages in a specific conversation for a user
        """
        # Verify the user has access to the conversation
        ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=conversation_id,
            owner_id=user_id
        )

        from uuid import UUID
        conversation_uuid = UUID(conversation_id)

        query = select(Message).where(Message.conversation_id == conversation_uuid).order_by(Message.created_at)

        # Get total count for pagination
        count_query = select(Message).where(Message.conversation_id == conversation_uuid)
        total = len(session.exec(count_query).all())

        # Apply pagination
        query = query.offset(offset).limit(limit)
        messages = session.exec(query).all()

        return messages, total

    @staticmethod
    def update_message(session: Session, message_id: str, message_data: MessageUpdate, user_id: str) -> Message:
        """
        Update a specific message for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(message_id) if isinstance(message_id, str) and message_id else message_id
        message = session.get(Message, uuid_obj)
        if not message:
            raise MessageNotFoundException(message_id)

        # Verify the user has access to the conversation that contains this message
        ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=str(message.conversation_id),
            owner_id=user_id
        )

        # Update message fields
        for field, value in message_data.dict(exclude_unset=True).items():
            setattr(message, field, value)

        session.add(message)
        session.commit()
        session.refresh(message)

        logger.info(f"Updated message {message.id} in conversation {message.conversation_id}")
        return message

    @staticmethod
    def delete_message(session: Session, message_id: str, user_id: str) -> bool:
        """
        Delete a specific message for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(message_id) if isinstance(message_id, str) and message_id else message_id
        message = session.get(Message, uuid_obj)
        if not message:
            raise MessageNotFoundException(message_id)

        # Verify the user has access to the conversation that contains this message
        ConversationService.get_conversation_by_id(
            session=session,
            conversation_id=str(message.conversation_id),
            owner_id=user_id
        )

        session.delete(message)
        session.commit()

        logger.info(f"Deleted message {message.id} from conversation {message.conversation_id}")
        return True