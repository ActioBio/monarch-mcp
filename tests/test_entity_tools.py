# tests/test_entity_tools.py
import pytest
from monarch_mcp.tools.entity import EntityApi

@pytest.mark.asyncio
async def test_get_entity(mock_client):
    """Test that get_entity calls the correct endpoint."""
    entity_api = EntityApi()
    entity_id = "MONDO:0005015"
    await entity_api.get_entity(mock_client, entity_id)
    mock_client.get.assert_called_once_with(f"entity/{entity_id}")

@pytest.mark.asyncio
async def test_get_entity_associations_by_category(mock_client):
    """Test that get_entity_associations_by_category calls the correct endpoint."""
    entity_api = EntityApi()
    entity_id = "MONDO:0005015"
    category = "biolink:DiseaseToPhenotypicFeatureAssociation"
    await entity_api.get_entity_associations_by_category(mock_client, entity_id, category, limit=10)
    expected_url = f"entity/{entity_id}/{category}"
    mock_client.get.assert_called_once_with(
        expected_url,
        params={"limit": 10, "offset": 0},
    )

@pytest.mark.asyncio
async def test_get_associations(mock_client):
    """Test that get_associations calls the correct generic association endpoint."""
    entity_api = EntityApi()
    subject_id = "MONDO:0005015"
    category = "biolink:DiseaseToPhenotypicFeatureAssociation"
    await entity_api.get_associations(mock_client, subject=[subject_id], category=[category], limit=10)
    mock_client.get.assert_called_once_with(
        "association",
        params={
            "subject": [subject_id],
            "category": [category],
            "limit": 10,
            "offset": 0,
            "direct": False
        },
    )