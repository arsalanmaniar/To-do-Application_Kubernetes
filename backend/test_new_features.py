"""
Basic tests to verify the new features have been integrated properly
"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool
from app.main import create_app
from app.models.user import User
from app.models.project import Project
from app.models.team import Team
from app.models.calendar_event import CalendarEvent
from app.models.conversation import Conversation
from app.models.message import Message


@pytest.fixture(name="engine")
def fixture_engine():
    """Create an in-memory SQLite engine for testing"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(bind=engine)
    return engine


@pytest.fixture(name="session")
def fixture_session(engine):
    """Create a test session"""
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def fixture_client(engine):
    """Create a test client"""
    def override_get_db_session():
        with Session(engine) as session:
            yield session

    app = create_app()

    # Override the dependency
    from app.core.dependencies import get_db_session
    app.dependency_overrides[get_db_session] = override_get_db_session

    client = TestClient(app)
    return client


def test_project_endpoints_exist(client):
    """Test that project endpoints are available"""
    # Test GET /projects (should return empty list with proper structure)
    response = client.get("/api/v1/projects")
    assert response.status_code in [200, 401]  # 401 is expected without auth token

    # Test POST /projects (should return validation error without proper data)
    response = client.post("/api/v1/projects", json={})
    assert response.status_code in [401, 422]  # 401 without auth, 422 without data


def test_team_endpoints_exist(client):
    """Test that team endpoints are available"""
    # Test GET /teams (should return empty list with proper structure)
    response = client.get("/api/v1/teams")
    assert response.status_code in [200, 401]  # 401 is expected without auth token

    # Test POST /teams (should return validation error without proper data)
    response = client.post("/api/v1/teams", json={})
    assert response.status_code in [401, 422]  # 401 without auth, 422 without data


def test_calendar_endpoints_exist(client):
    """Test that calendar endpoints are available"""
    # Test GET /calendar (should return empty list with proper structure)
    response = client.get("/api/v1/calendar")
    assert response.status_code in [200, 401]  # 401 is expected without auth token

    # Test POST /calendar (should return validation error without proper data)
    response = client.post("/api/v1/calendar", json={})
    assert response.status_code in [401, 422]  # 401 without auth, 422 without data


def test_conversation_endpoints_exist(client):
    """Test that conversation endpoints are available"""
    # Test GET /conversations (should return empty list with proper structure)
    response = client.get("/api/v1/conversations")
    assert response.status_code in [200, 401]  # 401 is expected without auth token

    # Test POST /conversations (should return validation error without proper data)
    response = client.post("/api/v1/conversations", json={})
    assert response.status_code in [401, 422]  # 401 without auth, 422 without data


def test_message_endpoints_exist(client):
    """Test that message endpoints are available"""
    # Test POST /messages (should return validation error without proper data)
    response = client.post("/api/v1/messages", json={})
    assert response.status_code in [401, 422]  # 401 without auth, 422 without data


def test_mcp_server_initialization():
    """Test that MCP server can be initialized"""
    from app.mcp.server import MCPServer
    mcp_server = MCPServer()
    assert mcp_server is not None
    assert mcp_server.config is not None


def test_ai_service_initialization():
    """Test that AI service can be initialized"""
    from app.services.ai_service import AIService
    ai_service = AIService()
    assert ai_service is not None


def test_new_models_can_be_created(session):
    """Test that new models can be instantiated"""
    # Test Project model
    project = Project(
        name="Test Project",
        description="A test project",
        owner_id="test_user_id"
    )
    session.add(project)
    session.commit()
    session.refresh(project)

    assert project.id is not None
    assert project.name == "Test Project"

    # Test Team model
    team = Team(
        name="Test Team",
        description="A test team",
        owner_id="test_user_id"
    )
    session.add(team)
    session.commit()
    session.refresh(team)

    assert team.id is not None
    assert team.name == "Test Team"


if __name__ == "__main__":
    pytest.main([__file__])