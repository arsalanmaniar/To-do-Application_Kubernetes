# Environment Variables for AI-Powered Todo Dashboard

## Required Variables

### Database Configuration
- `DATABASE_URL`: Connection string for Neon Serverless PostgreSQL database
  - Example: `postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require`

### Authentication
- `SECRET_KEY`: Secret key for JWT token encryption
  - Example: `your-super-secret-key-here-must-be-at-least-32-characters-long`
- `ALGORITHM`: Algorithm used for JWT encoding (default: `HS256`)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes (default: `30`)

### MCP Server Configuration
- `MCP_ENABLED`: Whether MCP integration is enabled (default: `false`)
- `MCP_HOST`: Host for MCP server (default: `localhost`)
- `MCP_PORT`: Port for MCP server (default: `8001`)
- `MCP_REQUEST_TIMEOUT`: Request timeout for MCP operations (default: `30`)
- `MCP_REQUIRE_AUTH`: Whether MCP requires authentication (default: `true`)
- `MCP_API_KEY`: API key for MCP authentication (required if `MCP_REQUIRE_AUTH` is true)

### AI Integration
- `OPENAI_API_KEY`: API key for OpenAI services (required for AI features)
  - Example: `sk-...`

## Optional Variables

### Logging
- `LOG_LEVEL`: Logging level (default: `INFO`)
- `LOG_FILE`: Path to log file (default: `app.log`)

### Development
- `DEBUG`: Enable debug mode (default: `false`)
- `TESTING`: Enable testing mode (default: `false`)

## Example .env File

```env
# Database
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require

# Authentication
SECRET_KEY=your-super-secret-key-here-must-be-at-least-32-characters-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# MCP Server
MCP_ENABLED=true
MCP_HOST=localhost
MCP_PORT=8001
MCP_REQUEST_TIMEOUT=30
MCP_REQUIRE_AUTH=true
MCP_API_KEY=your-mcp-api-key

# AI Integration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Logging
LOG_LEVEL=INFO
LOG_FILE=app.log

# Development
DEBUG=false
TESTING=false
```