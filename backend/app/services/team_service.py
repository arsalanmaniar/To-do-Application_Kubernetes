from sqlmodel import Session, select
from typing import List, Optional
from app.models.team import Team, TeamCreate, TeamUpdate
from app.core.exceptions import TeamNotFoundException, UnauthorizedAccessException
from app.core.logging import logger


class TeamService:
    """
    Service class for handling team-related operations
    """

    @staticmethod
    def create_team(session: Session, team_data: TeamCreate, owner_id: str) -> Team:
        """
        Create a new team for a user
        """
        team = Team(
            name=team_data.name,
            description=team_data.description,
            owner_id=owner_id
        )
        session.add(team)
        session.commit()
        session.refresh(team)

        logger.info(f"Created team {team.id} for user {owner_id}")
        return team

    @staticmethod
    def get_team_by_id(session: Session, team_id: str, owner_id: str) -> Team:
        """
        Get a specific team by ID for a specific user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(team_id) if isinstance(team_id, str) and team_id else team_id
        team = session.get(Team, uuid_obj)
        if not team:
            raise TeamNotFoundException(team_id)

        if team.owner_id != owner_id:
            raise UnauthorizedAccessException()

        return team

    @staticmethod
    def get_teams_by_user(
        session: Session,
        owner_id: str,
        limit: int = 50,
        offset: int = 0
    ) -> tuple[List[Team], int]:
        """
        Get all teams for a specific user
        """
        query = select(Team).where(Team.owner_id == owner_id)

        # Get total count for pagination
        count_query = select(Team).where(Team.owner_id == owner_id)
        total = len(session.exec(count_query).all())

        # Apply pagination
        query = query.offset(offset).limit(limit)
        teams = session.exec(query).all()

        return teams, total

    @staticmethod
    def update_team(session: Session, team_id: str, team_data: TeamUpdate, owner_id: str) -> Team:
        """
        Update a specific team for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(team_id) if isinstance(team_id, str) and team_id else team_id
        team = session.get(Team, uuid_obj)
        if not team:
            raise TeamNotFoundException(team_id)

        if team.owner_id != owner_id:
            raise UnauthorizedAccessException()

        # Update team fields
        for field, value in team_data.dict(exclude_unset=True).items():
            setattr(team, field, value)

        team.updated_at = type(team.updated_at).utcnow()  # Update timestamp

        session.add(team)
        session.commit()
        session.refresh(team)

        logger.info(f"Updated team {team.id} for user {owner_id}")
        return team

    @staticmethod
    def delete_team(session: Session, team_id: str, owner_id: str) -> bool:
        """
        Delete a specific team for a user
        """
        from uuid import UUID
        # Convert string ID to UUID object for proper database query
        uuid_obj = UUID(team_id) if isinstance(team_id, str) and team_id else team_id
        team = session.get(Team, uuid_obj)
        if not team:
            raise TeamNotFoundException(team_id)

        if team.owner_id != owner_id:
            raise UnauthorizedAccessException()

        session.delete(team)
        session.commit()

        logger.info(f"Deleted team {team.id} for user {owner_id}")
        return True