# tests/test_disease_tools.py
import pytest
from unittest.mock import patch, AsyncMock
from monarch_mcp.tools.disease import DiseaseApi

@pytest.mark.asyncio
async def test_get_disease_phenotype_associations(mock_client):
    """Test disease to phenotype associations call."""
    disease_api = DiseaseApi()
    disease_id = "MONDO:0005015"
    with patch.object(disease_api.entity_api, "get_associations", new_callable=AsyncMock) as mock_get_assoc:
        await disease_api.get_disease_phenotype_associations(mock_client, disease_id=disease_id, limit=5)
        mock_get_assoc.assert_called_once_with(
            mock_client,
            subject=[disease_id],
            category=["biolink:DiseaseToPhenotypicFeatureAssociation"],
            limit=5,
            offset=0
        )

@pytest.mark.asyncio
async def test_get_disease_gene_associations(mock_client):
    """Test disease to gene associations call."""
    disease_api = DiseaseApi()
    disease_id = "MONDO:0005015"
    with patch.object(disease_api.entity_api, "get_associations", new_callable=AsyncMock) as mock_get_assoc:
        await disease_api.get_disease_gene_associations(mock_client, disease_id=disease_id, limit=10)
        mock_get_assoc.assert_called_once_with(
            mock_client,
            subject=[disease_id],
            category=["biolink:CausalGeneToDiseaseAssociation", "biolink:CorrelatedGeneToDiseaseAssociation"],
            limit=10,
            offset=0
        )