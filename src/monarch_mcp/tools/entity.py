# src/monarch_mcp/tools/entity.py
from typing import Any, Dict, List, Optional
import mcp.types as types
from ..client import MonarchClient

class EntityApi:
    """
    Core tool for retrieving entities and their associations from the Monarch API.
    """

    async def get_entity(self, client: MonarchClient, entity_id: str) -> Dict[str, Any]:
        """
        Retrieves the entity with the specified ID.
        Args:
            entity_id (str): The CURIE of the entity to retrieve (e.g., "MONDO:0019391").
        """
        # CORRECT: Path is relative to the base_url in the client.
        return await client.get(f"entity/{entity_id}")

    async def get_entity_associations_by_category(
        self,
        client: MonarchClient,
        entity_id: str,
        category: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        Retrieves association data for a given entity and association category.
        Args:
            entity_id (str): ID of the entity to retrieve association data for.
            category (str): Category of association to retrieve.
        """
        # CORRECT: This now correctly maps to the /entity/{id}/{category} endpoint.
        params = {"limit": limit, "offset": offset}
        return await client.get(f"entity/{entity_id}/{category}", params=params)

    async def get_associations(
        self,
        client: MonarchClient,
        category: Optional[List[str]] = None,
        subject: Optional[List[str]] = None,
        predicate: Optional[List[str]] = None,
        object: Optional[List[str]] = None,
        entity: Optional[List[str]] = None,
        direct: bool = False,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Retrieves associations using the generic /association endpoint.
        Args:
            category: A list of association categories to filter for.
            subject: A list of subject CURIEs to filter for.
            predicate: A list of predicate CURIEs to filter for.
            object: A list of object CURIEs to filter for.
            entity: A list of entity CURIEs to filter for, in any position.
            direct: Whether to only return direct associations.
            limit: The number of associations to return.
            offset: The offset for pagination.
        """
        params = {
            "category": category,
            "subject": subject,
            "predicate": predicate,
            "object": object,
            "entity": entity,
            "direct": direct,
            "limit": limit,
            "offset": offset,
        }
        params = {k: v for k, v in params.items() if v is not None}
        # CORRECT: Path is relative to the base_url in the client.
        return await client.get("association", params=params)

ENTITY_TOOLS = [
    types.Tool(
        name="get_entity",
        description="Get detailed information about any Monarch entity (disease, phenotype, gene, etc.) by its ID.",
        inputSchema={
            "type": "object",
            "properties": {
                "entity_id": {"type": "string", "description": "Entity ID (e.g., MONDO:0005015, HP:0001250, HGNC:1097)"}
            },
            "required": ["entity_id"]
        }
    ),
    types.Tool(
        name="get_entity_associations_by_category",
        description="Retrieves a table of associations for a given entity, filtered by a single high-level category.",
        inputSchema={
            "type": "object",
            "properties": {
                "entity_id": {"type": "string", "description": "The ID of the entity, e.g., 'MONDO:0019391'"},
                "category": {"type": "string", "description": "The category of association table to retrieve."},
                "limit": {"type": "number", "description": "Number of results per page (default: 20)", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination (default: 0)", "default": 0}
            },
            "required": ["entity_id", "category"]
        }
    ),
    types.Tool(
        name="get_associations",
        description="Retrieves associations with powerful filtering, such as by subject, predicate, or object.",
        inputSchema={
            "type": "object",
            "properties": {
                "category": {"type": "array", "items": {"type": "string"}, "description": "A list of association categories to filter for."},
                "subject": {"type": "array", "items": {"type": "string"}, "description": "A list of subject CURIEs to filter for."},
                "predicate": {"type": "array", "items": {"type": "string"}, "description": "A list of predicate CURIEs to filter for."},
                "object": {"type": "array", "items": {"type": "string"}, "description": "A list of object CURIEs to filter for."},
                "entity": {"type": "array", "items": {"type": "string"}, "description": "A list of entity CURIEs to filter for, in any position."},
                "direct": {"type": "boolean", "description": "Whether to only return direct associations.", "default": False},
                "limit": {"type": "number", "description": "Number of results per page.", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination.", "default": 0}
            }
        }
    )
]