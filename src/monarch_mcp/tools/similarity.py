# src/monarch_mcp/tools/similarity.py
from typing import Any, Dict, List, Optional
import mcp.types as types
from ..client import MonarchClient

class SimilarityApi:
    """
    Semantic similarity calculations between entities, refactored for the v3 API.
    """

    async def compare_termsets(
        self,
        client: MonarchClient,
        subjects: List[str],
        objects: List[str],
        metric: str = "ancestor_information_content",
    ) -> Dict[str, Any]:
        """
        Get pairwise similarity between two sets of terms.
        Args:
            subjects: A list of subject CURIEs for comparison.
            objects: A list of object CURIEs for comparison.
            metric: The similarity metric to use.
        """
        subjects_str = ",".join(subjects)
        objects_str = ",".join(objects)
        params = {"metric": metric}
        return await client.get(f"semsim/compare/{subjects_str}/{objects_str}", params=params)

    async def find_similar_terms(
        self,
        client: MonarchClient,
        termset: List[str],
        search_group: str,
        metric: str = "ancestor_information_content",
        limit: int = 10,
    ) -> Dict[str, Any]:
        """
        Search for terms in a termset that are similar to a group of entities.
        Args:
            termset: Comma separated list of term IDs to find matches for.
            search_group: Group of entities to search within.
            metric: The similarity metric to use.
            limit: The number of results to return.
        """
        termset_str = ",".join(termset)
        params = {"metric": metric, "limit": limit}
        return await client.get(f"semsim/search/{termset_str}/{search_group}", params=params)


SIMILARITY_TOOLS = [
    types.Tool(
        name="compare_termsets",
        description="Calculate pairwise semantic similarity between two sets of entities (diseases, phenotypes, etc.).",
        inputSchema={
            "type": "object",
            "properties": {
                "subjects": {"type": "array", "items": {"type": "string"}, "description": "List of subject entity IDs"},
                "objects": {"type": "array", "items": {"type": "string"}, "description": "List of object entity IDs"},
                "metric": {
                    "type": "string",
                    "description": "The similarity metric to use.",
                    "default": "ancestor_information_content",
                    "enum": ["ancestor_information_content", "jaccard_similarity", "phenodigm_score"]
                }
            },
            "required": ["subjects", "objects"]
        }
    ),
    types.Tool(
        name="find_similar_terms",
        description="Find entities from a group that are semantically similar to a given set of terms.",
        inputSchema={
            "type": "object",
            "properties": {
                "termset": {"type": "array", "items": {"type": "string"}, "description": "List of entity IDs to find similar entities for"},
                "search_group": {
                    "type": "string",
                    "description": "Group of entities to search within.",
                    "enum": ["Human Diseases", "Mouse Genes", "Rat Genes", "Zebrafish Genes", "C. Elegans Genes"]
                },
                "metric": {
                    "type": "string",
                    "description": "The similarity metric to use.",
                    "default": "ancestor_information_content",
                    "enum": ["ancestor_information_content", "jaccard_similarity", "phenodigm_score"]
                },
                "limit": {"type": "number", "description": "Number of similar entities to return.", "default": 10}
            },
            "required": ["termset", "search_group"]
        }
    )
]