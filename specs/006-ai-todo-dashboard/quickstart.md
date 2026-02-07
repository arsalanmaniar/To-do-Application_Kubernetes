# Quickstart Guide: AI-Powered Todo Dashboard - Enhanced

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for backend)
- Neon Serverless PostgreSQL account
- OpenAI API key (for future AI features)
- Git

## Setup Instructions

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd hackathon-phase-3
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Update .env with your Neon DB URL, OpenAI key, etc.
```

### 3. Frontend Setup
```bash
# From project root
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.example .env.local
# Update with your backend API URL
```

### 4. Database Setup
```bash
# From backend directory
cd backend
source venv/bin/activate

# Run database migrations (tables will be created automatically on startup)
python -m src.database.migrate
```

### 5. Running the Application

**Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=your_neon_db_url
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_key  # For future AI features
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/sign-up` - Register new user (alias)
- `POST /auth/login` - Login user
- `POST /auth/sign-in` - Login user (alias)
- `GET /auth/me` - Get user profile

### Tasks
- `GET /api/v1/tasks` - Get user's tasks
- `POST /api/v1/tasks` - Create new task
- `GET /api/v1/tasks/{id}` - Get specific task
- `PUT /api/v1/tasks/{id}` - Update task completely
- `PATCH /api/v1/tasks/{id}` - Update task partially
- `PATCH /api/v1/tasks/{id}/complete` - Toggle task completion
- `DELETE /api/v1/tasks/{id}` - Delete task

### Projects (NEW)
- `GET /api/v1/projects` - Get user's projects
- `POST /api/v1/projects` - Create new project
- `GET /api/v1/projects/{id}` - Get specific project
- `PUT /api/v1/projects/{id}` - Update project
- `DELETE /api/v1/projects/{id}` - Delete project

### Teams (NEW)
- `GET /api/v1/teams` - Get user's teams
- `POST /api/v1/teams` - Create new team
- `GET /api/v1/teams/{id}` - Get specific team
- `PUT /api/v1/teams/{id}` - Update team
- `DELETE /api/v1/teams/{id}` - Delete team

### Calendar Events (NEW)
- `GET /api/v1/calendar` - Get user's calendar events
- `POST /api/v1/calendar` - Create new calendar event
- `GET /api/v1/calendar/{id}` - Get specific event
- `PUT /api/v1/calendar/{id}` - Update event
- `DELETE /api/v1/calendar/{id}` - Delete event

## Development Commands

### Backend
```bash
# Run tests
pytest

# Format code
black .

# Check types
mypy .
```

### Frontend
```bash
# Run tests
npm test

# Build for production
npm run build
```

## MCP Server Preparation

The backend is prepared for MCP server integration to support AI features. Future implementation will include:
- MCP protocol endpoints
- AI agent communication layer
- Conversation state management