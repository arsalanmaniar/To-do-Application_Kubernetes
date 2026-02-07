from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import Optional
from app.services.calendar_service import CalendarEventService
from app.schemas.calendar_event import (
    CalendarEventCreate, CalendarEventRead, CalendarEventUpdate, CalendarEventListResponse
)
from app.core.dependencies import get_current_user_id, get_db_session
from app.core.logging import logger
from datetime import datetime, date
import uuid

router = APIRouter()


@router.get("/calendar", response_model=CalendarEventListResponse)
def get_calendar_events(
    current_user_id: str = Depends(get_current_user_id),
    start_date: Optional[date] = Query(None, description="Filter events starting from this date"),
    end_date: Optional[date] = Query(None, description="Filter events ending before this date"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve all calendar events for the specified user with optional date filtering
    """
    try:
        # Convert date to datetime for comparison
        start_datetime = None
        end_datetime = None
        if start_date:
            start_datetime = datetime.combine(start_date, datetime.min.time())
        if end_date:
            end_datetime = datetime.combine(end_date, datetime.max.time())

        events, total = CalendarEventService.get_calendar_events_by_user(
            session=session,
            owner_id=current_user_id,
            start_date=start_datetime,
            end_date=end_datetime,
            limit=limit,
            offset=offset
        )

        event_responses = []
        for event in events:
            event_response = CalendarEventRead(
                id=event.id,
                title=event.title,
                description=event.description,
                start_time=event.start_time,
                end_time=event.end_time,
                all_day=event.all_day,
                owner_id=event.owner_id,
                task_id=event.task_id,
                created_at=event.created_at,
                updated_at=event.updated_at
            )
            event_responses.append(event_response)

        return CalendarEventListResponse(
            events=event_responses,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        logger.error(f"Error getting calendar events for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/calendar", response_model=CalendarEventRead, status_code=201)
def create_calendar_event(
    event_data: CalendarEventCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new calendar event for the current user
    """
    try:
        event = CalendarEventService.create_calendar_event(
            session=session,
            event_data=event_data,
            owner_id=current_user_id
        )

        return CalendarEventRead(
            id=event.id,
            title=event.title,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time,
            all_day=event.all_day,
            owner_id=event.owner_id,
            task_id=event.task_id,
            created_at=event.created_at,
            updated_at=event.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating calendar event for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/calendar/{event_id}", response_model=CalendarEventRead)
def get_calendar_event(
    event_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve a specific calendar event by ID
    """
    try:
        event = CalendarEventService.get_calendar_event_by_id(
            session=session,
            event_id=event_id,
            owner_id=current_user_id
        )

        return CalendarEventRead(
            id=event.id,
            title=event.title,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time,
            all_day=event.all_day,
            owner_id=event.owner_id,
            task_id=event.task_id,
            created_at=event.created_at,
            updated_at=event.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting calendar event {event_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/calendar/{event_id}", response_model=CalendarEventRead)
def update_calendar_event(
    event_id: str,
    event_data: CalendarEventUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific calendar event completely
    """
    try:
        event = CalendarEventService.update_calendar_event(
            session=session,
            event_id=event_id,
            event_data=event_data,
            owner_id=current_user_id
        )

        return CalendarEventRead(
            id=event.id,
            title=event.title,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time,
            all_day=event.all_day,
            owner_id=event.owner_id,
            task_id=event.task_id,
            created_at=event.created_at,
            updated_at=event.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating calendar event {event_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/calendar/{event_id}", response_model=CalendarEventRead)
def patch_calendar_event(
    event_id: str,
    event_data: CalendarEventUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Partially update a specific calendar event
    """
    try:
        event = CalendarEventService.update_calendar_event(
            session=session,
            event_id=event_id,
            event_data=event_data,
            owner_id=current_user_id
        )

        return CalendarEventRead(
            id=event.id,
            title=event.title,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time,
            all_day=event.all_day,
            owner_id=event.owner_id,
            task_id=event.task_id,
            created_at=event.created_at,
            updated_at=event.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error patching calendar event {event_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/calendar/{event_id}", status_code=204)
def delete_calendar_event(
    event_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific calendar event
    """
    try:
        CalendarEventService.delete_calendar_event(
            session=session,
            event_id=event_id,
            owner_id=current_user_id
        )
        return
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting calendar event {event_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")