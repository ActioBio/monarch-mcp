# tests/test_mapping_tools.py
import pytest
from monarch_mcp.tools.mapping import MappingApi

@pytest.mark.asyncio
async def test_get_mappings(mock_client):
    """Test that get_mappings calls the correct endpoint."""
    mapping_api = MappingApi()
    entity_id = "MONDO:0019391"
    predicate_id = "skos:exactMatch"
    await mapping_api.get_mappings(mock_client, entity_id=[entity_id], predicate_id=[predicate_id])
    mock_client.get.assert_called_once_with(
        "mappings",
        params={
            "entity_id": [entity_id],
            "predicate_id": [predicate_id],
            "limit": 20,
            "offset": 0
        },
    )