from sqlmodel import Session, select
from typing import List, Optional
from app.models.calendar_event import CalendarEvent, CalendarEventCreate, CalendarEventUpdate
from app.core.exceptions import CalendarEventNotFoundException, UnauthorizedAccessException
from app.core.logging import logger
from datetime import datetime


class CalendarEventService:
    """
    Service class for handling calendar event-related operations
    """

    @staticmethod
    def create_calendar_event(session: Session, event_data: CalendarEventCreate, owner_id: str) -> CalendarEvent:
        """
        Create a new calendar event for a user
        """
        # Validate that start_time is before end_time
        if event_data.start_time >= event_data.end_time:
            raise ValueError("Start time must be before end time")

        event = CalendarEvent(
            title=event_data.title,
            description=event_data.description,
            start_time=event_data.start_time,
            end_time=event_data.end_time,
            all_day=event_data.all_day,
            owner_id=owner_id,
            task_id=event_data.task_id
        )
        session.add(event)
        session.commit()
        session.refresh(event)

        logger.info(f"Created calendar event {event.id} for user {owner_id}")
        return event

    @staticmethod
    def get_calendar_event_by_id(session: Session, event_id: str, owner_id: str) -> CalendarEvent:
        """
        Get a specific calendar event by ID for a specific user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(event_id) if isinstance(event_id, str) and event_id else event_id
        event = session.get(CalendarEvent, uuid_obj)
        if not event:
            raise CalendarEventNotFoundException(event_id)

        if event.owner_id != owner_id:
            raise UnauthorizedAccessException()

        return event

    @staticmethod
    def get_calendar_events_by_user(
        session: Session,
        owner_id: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[List[CalendarEvent], int]:
        """
        Get all calendar events for a specific user with optional date filtering
        """
        query = select(CalendarEvent).where(CalendarEvent.owner_id == owner_id)

        # Apply date filters if provided
        if start_date:
            query = query.where(CalendarEvent.start_time >= start_date)
        if end_date:
            query = query.where(CalendarEvent.end_time <= end_date)

        # Get total count for pagination
        count_query = select(CalendarEvent).where(CalendarEvent.owner_id == owner_id)
        if start_date:
            count_query = count_query.where(CalendarEvent.start_time >= start_date)
        if end_date:
            count_query = count_query.where(CalendarEvent.end_time <= end_date)
        total = len(session.exec(count_query).all())

        # Apply pagination
        query = query.offset(offset).limit(limit).order_by(CalendarEvent.start_time)
        events = session.exec(query).all()

        return events, total

    @staticmethod
    def update_calendar_event(session: Session, event_id: str, event_data: CalendarEventUpdate, owner_id: str) -> CalendarEvent:
        """
        Update a specific calendar event for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(event_id) if isinstance(event_id, str) and event_id else event_id
        event = session.get(CalendarEvent, uuid_obj)
        if not event:
            raise CalendarEventNotFoundException(event_id)

        if event.owner_id != owner_id:
            raise UnauthorizedAccessException()

        # Validate time constraints if updating time fields
        start_time = event_data.start_time or event.start_time
        end_time = event_data.end_time or event.end_time
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")

        # Update event fields
        for field, value in event_data.dict(exclude_unset=True).items():
            setattr(event, field, value)

        event.updated_at = type(event.updated_at).utcnow()  # Update timestamp

        session.add(event)
        session.commit()
        session.refresh(event)

        logger.info(f"Updated calendar event {event.id} for user {owner_id}")
        return event

    @staticmethod
    def delete_calendar_event(session: Session, event_id: str, owner_id: str) -> bool:
        """
        Delete a specific calendar event for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(event_id) if isinstance(event_id, str) and event_id else event_id
        event = session.get(CalendarEvent, uuid_obj)
        if not event:
            raise CalendarEventNotFoundException(event_id)

        if event.owner_id != owner_id:
            raise UnauthorizedAccessException()

        session.delete(event)
        session.commit()

        logger.info(f"Deleted calendar event {event.id} for user {owner_id}")
        return True