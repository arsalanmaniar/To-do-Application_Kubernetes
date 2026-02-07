from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from typing import Optional
from app.services.team_service import TeamService
from app.schemas.team import (
    TeamCreate, TeamRead, TeamUpdate, TeamListResponse
)
from app.core.dependencies import get_current_user_id, get_db_session
from app.core.logging import logger
from datetime import datetime
import uuid

router = APIRouter()


@router.get("/teams", response_model=TeamListResponse)
def get_teams(
    current_user_id: str = Depends(get_current_user_id),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve all teams for the specified user
    """
    try:
        teams, total = TeamService.get_teams_by_user(
            session=session,
            owner_id=current_user_id,
            limit=limit,
            offset=offset
        )

        team_responses = []
        for team in teams:
            team_response = TeamRead(
                id=team.id,
                name=team.name,
                description=team.description,
                owner_id=team.owner_id,
                created_at=team.created_at,
                updated_at=team.updated_at
            )
            team_responses.append(team_response)

        return TeamListResponse(
            teams=team_responses,
            total=total,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        logger.error(f"Error getting teams for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/teams", response_model=TeamRead, status_code=201)
def create_team(
    team_data: TeamCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new team for the current user
    """
    try:
        team = TeamService.create_team(
            session=session,
            team_data=team_data,
            owner_id=current_user_id
        )

        return TeamRead(
            id=team.id,
            name=team.name,
            description=team.description,
            owner_id=team.owner_id,
            created_at=team.created_at,
            updated_at=team.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating team for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/teams/{team_id}", response_model=TeamRead)
def get_team(
    team_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Retrieve a specific team by ID
    """
    try:
        team = TeamService.get_team_by_id(
            session=session,
            team_id=team_id,
            owner_id=current_user_id
        )

        return TeamRead(
            id=team.id,
            name=team.name,
            description=team.description,
            owner_id=team.owner_id,
            created_at=team.created_at,
            updated_at=team.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting team {team_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/teams/{team_id}", response_model=TeamRead)
def update_team(
    team_id: str,
    team_data: TeamUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific team completely
    """
    try:
        team = TeamService.update_team(
            session=session,
            team_id=team_id,
            team_data=team_data,
            owner_id=current_user_id
        )

        return TeamRead(
            id=team.id,
            name=team.name,
            description=team.description,
            owner_id=team.owner_id,
            created_at=team.created_at,
            updated_at=team.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating team {team_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/teams/{team_id}", response_model=TeamRead)
def patch_team(
    team_id: str,
    team_data: TeamUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Partially update a specific team
    """
    try:
        team = TeamService.update_team(
            session=session,
            team_id=team_id,
            team_data=team_data,
            owner_id=current_user_id
        )

        return TeamRead(
            id=team.id,
            name=team.name,
            description=team.description,
            owner_id=team.owner_id,
            created_at=team.created_at,
            updated_at=team.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error patching team {team_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/teams/{team_id}", status_code=204)
def delete_team(
    team_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific team
    """
    try:
        TeamService.delete_team(
            session=session,
            team_id=team_id,
            owner_id=current_user_id
        )
        return
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting team {team_id} for user {current_user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")