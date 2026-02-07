from fastapi import Request, HTTPException
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from app.config.mcp_config import mcp_config
from app.core.logging import logger
import time


class MCPServerMiddleware(BaseHTTPMiddleware):
    """
    Middleware for handling MCP (Model Context Protocol) related requests
    This middleware intercepts requests and responses to enable AI integration
    """

    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        """
        Process the request through the MCP middleware
        """
        start_time = time.time()

        # Log incoming request for MCP debugging
        if mcp_config.enabled:
            logger.debug(f"MCP Middleware: Processing request {request.method} {request.url}")

        # Add MCP context to the request state
        request.state.mcp_enabled = mcp_config.enabled
        request.state.mcp_start_time = start_time

        # Process the request
        response = await call_next(request)

        # Add MCP-related headers to the response
        if mcp_config.enabled:
            processing_time = time.time() - start_time
            response.headers["X-MCP-Processing-Time"] = str(processing_time)
            response.headers["X-MCP-Enabled"] = str(mcp_config.enabled).lower()

        return response


async def verify_mcp_auth(request: Request) -> bool:
    """
    Verify MCP authentication if required
    """
    if not mcp_config.require_auth:
        return True

    # Check for API key in header
    api_key = request.headers.get("X-API-Key") or request.headers.get("Authorization")

    if not api_key:
        logger.warning("MCP request missing authentication header")
        return False

    if api_key != mcp_config.api_key:
        logger.warning("MCP request has invalid API key")
        return False

    return True


async def check_mcp_rate_limit(request: Request) -> bool:
    """
    Check MCP rate limits if configured
    """
    # Placeholder for rate limiting logic
    # In a real implementation, we would check request counts against limits
    return True