# src/monarch_mcp/tools/histopheno.py
from typing import Any, Dict
import mcp.types as types
from ..client import MonarchClient

class HistoPhenoApi:
    """
    Tool for retrieving histopheno data from the Monarch API.
    """

    async def get_histopheno(self, client: MonarchClient, id: str) -> Dict[str, Any]:
        """
        Retrieves histopheno data for a given entity ID.
        Args:
            id (str): The CURIE of the entity to retrieve histopheno data for.
        """
        return await client.get(f"histopheno/{id}")

HISTOPHENO_TOOLS = [
    types.Tool(
        name="get_histopheno",
        description="Retrieves histopheno data for a given entity ID.",
        inputSchema={
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "The CURIE of the entity (e.g., a disease ID)."}
            },
            "required": ["id"]
        }
    )
]