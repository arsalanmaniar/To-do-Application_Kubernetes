"""
Configuration for MCP (Model Context Protocol) server
"""

import os
from typing import Dict, Any, Optional


class MCPConfig:
    """
    Configuration class for MCP server settings
    """

    def __init__(self):
        # Enable/disable MCP integration
        self.enabled: bool = os.getenv("MCP_ENABLED", "false").lower() == "true"

        # MCP server settings
        self.host: str = os.getenv("MCP_HOST", "localhost")
        self.port: int = int(os.getenv("MCP_PORT", "8001"))

        # Timeout settings for MCP operations
        self.request_timeout: int = int(os.getenv("MCP_REQUEST_TIMEOUT", "30"))
        self.connection_timeout: int = int(os.getenv("MCP_CONNECTION_TIMEOUT", "10"))

        # Security settings
        self.require_auth: bool = os.getenv("MCP_REQUIRE_AUTH", "true").lower() == "true"
        self.api_key: Optional[str] = os.getenv("MCP_API_KEY")

        # Logging settings
        self.log_level: str = os.getenv("MCP_LOG_LEVEL", "INFO")
        self.log_file: Optional[str] = os.getenv("MCP_LOG_FILE")

        # Supported protocols
        self.supported_protocols: list = [
            "http",
            "websocket"
        ]

        # Registered tools configuration
        self.registered_tools: Dict[str, Any] = {}

    def validate(self) -> bool:
        """
        Validate the configuration settings
        """
        if self.port < 1 or self.port > 65535:
            raise ValueError(f"Invalid port: {self.port}. Port must be between 1 and 65535.")

        if self.request_timeout <= 0:
            raise ValueError(f"Request timeout must be positive, got: {self.request_timeout}")

        if self.connection_timeout <= 0:
            raise ValueError(f"Connection timeout must be positive, got: {self.connection_timeout}")

        if self.require_auth and not self.api_key:
            raise ValueError("API key is required when auth is enabled")

        return True

    def get_settings(self) -> Dict[str, Any]:
        """
        Get all configuration settings as a dictionary
        """
        return {
            "enabled": self.enabled,
            "host": self.host,
            "port": self.port,
            "request_timeout": self.request_timeout,
            "connection_timeout": self.connection_timeout,
            "require_auth": self.require_auth,
            "log_level": self.log_level,
            "log_file": self.log_file,
            "supported_protocols": self.supported_protocols
        }


# Global configuration instance
mcp_config = MCPConfig()

# Validate configuration on import
try:
    mcp_config.validate()
except ValueError as e:
    print(f"Configuration error: {e}")
    raise