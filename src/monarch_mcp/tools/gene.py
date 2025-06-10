# src/monarch_mcp/tools/gene.py
from typing import Any, Dict
import mcp.types as types
from ..client import MonarchClient
from .entity import EntityApi

class GeneApi:
    """
    Gene-specific queries for Monarch, refactored to use the core associations API.
    """
    def __init__(self):
        self.entity_api = EntityApi()

    async def get_gene_phenotype_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get phenotypes associated with a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToPhenotypicFeatureAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_disease_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get diseases associated with a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToDiseaseAssociation"],
            limit=limit,
            offset=offset
        )

    async def get_gene_expression_associations(
        self,
        client: MonarchClient,
        gene_id: str,
        limit: int = 20,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get expression data for a gene."""
        return await self.entity_api.get_associations(
            client,
            subject=[gene_id],
            category=["biolink:GeneToExpressionSiteAssociation"],
            limit=limit,
            offset=offset
        )

GENE_TOOLS = [
    types.Tool(
        name="get_gene_phenotype_associations",
        description="Get phenotypes associated with a gene across species.",
        inputSchema={
            "type": "object",
            "properties": {
                "gene_id": {"type": "string", "description": "Gene ID (e.g., HGNC:1097 for BRCA1)"},
                "limit": {"type": "number", "description": "Number of results per page.", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination.", "default": 0}
            },
            "required": ["gene_id"]
        }
    ),
    types.Tool(
        name="get_gene_disease_associations",
        description="Get diseases associated with a gene.",
        inputSchema={
            "type": "object",
            "properties": {
                "gene_id": {"type": "string", "description": "Gene ID (e.g., HGNC:1097)"},
                "limit": {"type": "number", "description": "Number of results per page.", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination.", "default": 0}
            },
            "required": ["gene_id"]
        }
    ),
    types.Tool(
        name="get_gene_expression_associations",
        description="Get gene expression data across tissues and cell types.",
        inputSchema={
            "type": "object",
            "properties": {
                "gene_id": {"type": "string", "description": "Gene ID (e.g., HGNC:1097)"},
                "limit": {"type": "number", "description": "Number of results per page.", "default": 20},
                "offset": {"type": "number", "description": "Offset for pagination.", "default": 0}
            },
            "required": ["gene_id"]
        }
    )
]