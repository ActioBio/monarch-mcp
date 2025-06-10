import asyncio
import json
from typing import Any, Dict, Type
import logging
import os

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from .client import MonarchClient
from .tools import ALL_TOOLS, API_CLASS_MAP

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MonarchMcpServer:
    """
    MCP Server for Monarch Initiative data.
    """
    def __init__(self):
        self.server_name = "monarch-mcp"
        self.server_version = "0.1.0"
        self.mcp_server = Server(self.server_name, self.server_version)
        self.client = MonarchClient()
        self._api_instances: Dict[Type, Any] = {}
        self._setup_handlers()
        logger.info(f"{self.server_name} v{self.server_version} initialized.")

    def _setup_handlers(self):
        """Register MCP handlers."""
        
        @self.mcp_server.list_tools()
        async def handle_list_tools() -> list[types.Tool]:
            """Returns the list of all available tools."""
            return ALL_TOOLS

        @self.mcp_server.call_tool()
        async def handle_call_tool(
            name: str, arguments: Dict[str, Any]
        ) -> list[types.TextContent]:
            """Handles a tool call request."""
            logger.info(f"Handling call for tool: '{name}'")
            
            try:
                if name not in API_CLASS_MAP:
                    raise ValueError(f"Unknown tool: {name}")

                api_class = API_CLASS_MAP[name]
                
                if api_class not in self._api_instances:
                    self._api_instances[api_class] = api_class()
                
                api_instance = self._api_instances[api_class]
                
                if not hasattr(api_instance, name):
                    raise ValueError(f"Tool method '{name}' not found")
                
                func_to_call = getattr(api_instance, name)
                result_data = await func_to_call(self.client, **arguments)
                
                result_json = json.dumps(result_data, indent=2)
                return [types.TextContent(type="text", text=result_json)]

            except Exception as e:
                logger.error(f"Error calling tool '{name}': {str(e)}", exc_info=True)
                error_response = {
                    "error": type(e).__name__,
                    "message": str(e),
                    "tool_name": name
                }
                return [types.TextContent(type="text", text=json.dumps(error_response, indent=2))]

    async def run(self):
        """Starts the MCP server."""
        logger.info(f"Starting {self.server_name} v{self.server_version}...")
        
        async with stdio_server() as (read_stream, write_stream):
            await self.mcp_server.run(
                read_stream, 
                write_stream,
                self.mcp_server.create_initialization_options()
            )

def main():
    """Main entry point."""
    server = MonarchMcpServer()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("Server interrupted by user.")
    finally:
        asyncio.run(server.client.close())
        logger.info("Server shutdown complete.")

if __name__ == "__main__":
    main()