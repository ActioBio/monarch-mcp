# src/monarch_mcp/tools/search.py
from typing import Any, Dict, List, Optional
import mcp.types as types
from ..client import MonarchClient

class SearchApi:
    """
    Search and autocomplete functionality across Monarch entities, refactored for the v3 API.
    """

    async def search(
        self,
        client: MonarchClient,
        q: str,
        category: Optional[List[str]] = None,
        in_taxon_label: Optional[List[str]] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Search for entities by label, with optional filters.
        Args:
            q: The search query string.
            category: A list of Biolink model categories to filter by.
            in_taxon_label: A list of taxon labels to filter by.
            limit: The number of results to return.
            offset: The offset for pagination.
        """
        params = {
            "q": q,
            "category": category,
            "in_taxon_label": in_taxon_label,
            "limit": limit,
            "offset": offset,
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await client.get("search", params=params)

    async def autocomplete(self, client: MonarchClient, q: str) -> Dict[str, Any]:
        """
        Autocomplete for entities by label.
        Args:
            q: The query string to autocomplete against.
        """
        return await client.get("autocomplete", params={"q": q})

    async def semsim_autocomplete(self, client: MonarchClient, q: str) -> Dict[str, Any]:
        """
        Autocomplete for semantic similarity lookups.
        Args:
            q: The query string to autocomplete against.
        """
        return await client.get("semsim/autocomplete", params={"q": q})


SEARCH_TOOLS = [
    types.Tool(
        name="search",
        description="Search for entities (e.g., diseases, phenotypes, genes) by text query.",
        inputSchema={
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Search query text"},
                "category": {"type": "array", "items": {"type": "string"}, "description": "Filter by a list of Biolink categories (e.g., ['biolink:Disease'])."},
                "in_taxon_label": {"type": "array", "items": {"type": "string"}, "description": "Filter by a list of taxon labels (e.g., ['Homo sapiens'])."},
                "limit": {"type": "number", "description": "Number of results per page.", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination.", "default": 0}
            },
            "required": ["q"]
        }
    ),
    types.Tool(
        name="autocomplete",
        description="Get autocomplete suggestions for a partial query.",
        inputSchema={
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Partial search query for autocomplete"}
            },
            "required": ["q"]
        }
    ),
    types.Tool(
        name="semsim_autocomplete",
        description="Get autocomplete suggestions for semantic similarity lookups, prioritizing entities with direct phenotype associations.",
        inputSchema={
            "type": "object",
            "properties": {
                "q": {"type": "string", "description": "Partial search query for autocomplete"}
            },
            "required": ["q"]
        }
    )
]