from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self, user_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )


class TaskNotFoundException(HTTPException):
    def __init__(self, task_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )


class ProjectNotFoundException(HTTPException):
    def __init__(self, project_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found"
        )


class TeamNotFoundException(HTTPException):
    def __init__(self, team_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found"
        )


class CalendarEventNotFoundException(HTTPException):
    def __init__(self, event_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Calendar event with ID {event_id} not found"
        )


class ConversationNotFoundException(HTTPException):
    def __init__(self, conversation_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversation with ID {conversation_id} not found"
        )


class MessageNotFoundException(HTTPException):
    def __init__(self, message_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Message with ID {message_id} not found"
        )


class UnauthorizedAccessException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Insufficient permissions"
        )


class ValidationErrorException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )