from typing import Dict, Any, Callable
from abc import ABC, abstractmethod
import asyncio
import json
from app.core.logging import logger


class MCPTask:
    """
    Base class for MCP (Model Context Protocol) tasks
    This provides a standardized way to define and execute AI-related tasks
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the MCP task with given parameters
        """
        pass


class MCPTool:
    """
    Base class for MCP tools that can be used by AI agents
    """

    def __init__(self, name: str, description: str, parameters: Dict[str, Any]):
        self.name = name
        self.description = description
        self.parameters = parameters

    @abstractmethod
    async def call(self, params: Dict[str, Any]) -> Any:
        """
        Call the MCP tool with given parameters
        """
        pass


class MCPConfig:
    """
    Configuration for the MCP server
    """

    def __init__(self):
        self.tools: Dict[str, MCPTool] = {}
        self.tasks: Dict[str, MCPTask] = {}
        self.enabled = True  # Whether MCP integration is enabled


class MCPServer:
    """
    MCP (Model Context Protocol) Server for AI integration
    This provides a standardized interface for AI agents to interact with the backend
    """

    def __init__(self):
        self.config = MCPConfig()
        self.initialized = False

    async def initialize(self):
        """
        Initialize the MCP server and register tools
        """
        if self.initialized:
            return

        logger.info("Initializing MCP Server")

        # Register default tools
        await self.register_default_tools()

        self.initialized = True
        logger.info("MCP Server initialized successfully")

    async def register_tool(self, tool: MCPTool):
        """
        Register an MCP tool that can be used by AI agents
        """
        self.config.tools[tool.name] = tool
        logger.info(f"Registered MCP tool: {tool.name}")

    async def register_task(self, task: MCPTask):
        """
        Register an MCP task that can be executed by AI agents
        """
        self.config.tasks[task.name] = task
        logger.info(f"Registered MCP task: {task.name}")

    async def register_default_tools(self):
        """
        Register default tools for basic functionality
        """
        # This is where we would register default tools like task management, etc.
        # For now, this is a placeholder that will be expanded in future phases
        pass

    async def execute_task(self, task_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute an MCP task by name with given parameters
        """
        if not self.initialized:
            await self.initialize()

        if task_name not in self.config.tasks:
            raise ValueError(f"Task '{task_name}' not found")

        task = self.config.tasks[task_name]
        logger.info(f"Executing MCP task: {task_name}")

        result = await task.execute(params)
        logger.info(f"MCP task '{task_name}' completed successfully")

        return result

    async def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        """
        Call an MCP tool by name with given parameters
        """
        if not self.initialized:
            await self.initialize()

        if tool_name not in self.config.tools:
            raise ValueError(f"Tool '{tool_name}' not found")

        tool = self.config.tools[tool_name]
        logger.info(f"Calling MCP tool: {tool_name}")

        result = await tool.call(params)
        logger.info(f"MCP tool '{tool_name}' called successfully")

        return result

    def get_available_tools(self) -> Dict[str, str]:
        """
        Get a dictionary of available tools and their descriptions
        """
        return {name: tool.description for name, tool in self.config.tools.items()}

    def get_available_tasks(self) -> Dict[str, str]:
        """
        Get a dictionary of available tasks and their descriptions
        """
        return {name: task.description for name, task in self.config.tasks.items()}


# Global MCP server instance
mcp_server = MCPServer()


async def get_mcp_server() -> MCPServer:
    """
    Get the global MCP server instance, initializing it if needed
    """
    if not mcp_server.initialized:
        await mcp_server.initialize()
    return mcp_server