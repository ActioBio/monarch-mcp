# tests/test_search_tools.py
import pytest
from monarch_mcp.tools.search import SearchApi

@pytest.mark.asyncio
async def test_search(mock_client):
    """Test that search calls the correct endpoint with all parameters."""
    search_api = SearchApi()
    await search_api.search(
        mock_client,
        q="marfan",
        category=["biolink:Disease"],
        in_taxon_label=["Homo sapiens"],
        limit=5
    )
    mock_client.get.assert_called_once_with(
        "search",
        params={
            "q": "marfan",
            "category": ["biolink:Disease"],
            "in_taxon_label": ["Homo sapiens"],
            "limit": 5,
            "offset": 0
        },
    )

@pytest.mark.asyncio
async def test_autocomplete(mock_client):
    """Test that autocomplete calls the correct endpoint."""
    search_api = SearchApi()
    await search_api.autocomplete(mock_client, q="marf")
    mock_client.get.assert_called_once_with(
        "autocomplete",
        params={"q": "marf"}
    )

@pytest.mark.asyncio
async def test_semsim_autocomplete(mock_client):
    """Test that semsim_autocomplete calls the correct endpoint."""
    search_api = SearchApi()
    await search_api.semsim_autocomplete(mock_client, q="pheno")
    mock_client.get.assert_called_once_with(
        "semsim/autocomplete",
        params={"q": "pheno"}
    )