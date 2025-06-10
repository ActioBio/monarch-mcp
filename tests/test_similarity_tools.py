# tests/test_similarity_tools.py
import pytest
from monarch_mcp.tools.similarity import SimilarityApi

@pytest.mark.asyncio
async def test_compare_termsets(mock_client):
    """Test compare_termsets calls the correct semsim compare endpoint."""
    similarity_api = SimilarityApi()
    subjects = ["HP:0001250", "HP:0001290"]
    objects = ["MONDO:0005015", "MONDO:0007947"]
    
    await similarity_api.compare_termsets(mock_client, subjects=subjects, objects=objects)
    
    subjects_str = ",".join(subjects)
    objects_str = ",".join(objects)
    expected_url = f"semsim/compare/{subjects_str}/{objects_str}"
    
    mock_client.get.assert_called_once_with(
        expected_url,
        params={"metric": "ancestor_information_content"}
    )

@pytest.mark.asyncio
async def test_find_similar_terms(mock_client):
    """Test find_similar_terms calls the correct semsim search endpoint."""
    similarity_api = SimilarityApi()
    termset = ["HP:0001250"]
    search_group = "Human Diseases"
    
    await similarity_api.find_similar_terms(mock_client, termset=termset, search_group=search_group, limit=5)
    
    termset_str = ",".join(termset)
    expected_url = f"semsim/search/{termset_str}/{search_group}"
    
    mock_client.get.assert_called_once_with(
        expected_url,
        params={"metric": "ancestor_information_content", "limit": 5}
    )