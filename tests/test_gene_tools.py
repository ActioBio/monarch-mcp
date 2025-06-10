# tests/test_gene_tools.py
import pytest
from unittest.mock import patch, AsyncMock
from monarch_mcp.tools.gene import GeneApi

@pytest.mark.asyncio
async def test_get_gene_phenotype_associations(mock_client):
    """Test gene to phenotype associations call."""
    gene_api = GeneApi()
    gene_id = "HGNC:1097"
    with patch.object(gene_api.entity_api, "get_associations", new_callable=AsyncMock) as mock_get_assoc:
        await gene_api.get_gene_phenotype_associations(mock_client, gene_id=gene_id, limit=5)
        mock_get_assoc.assert_called_once_with(
            mock_client,
            subject=[gene_id],
            category=["biolink:GeneToPhenotypicFeatureAssociation"],
            limit=5,
            offset=0
        )

@pytest.mark.asyncio
async def test_get_gene_disease_associations(mock_client):
    """Test gene to disease associations call."""
    gene_api = GeneApi()
    gene_id = "HGNC:1097"
    with patch.object(gene_api.entity_api, "get_associations", new_callable=AsyncMock) as mock_get_assoc:
        await gene_api.get_gene_disease_associations(mock_client, gene_id=gene_id, limit=10)
        mock_get_assoc.assert_called_once_with(
            mock_client,
            subject=[gene_id],
            category=["biolink:GeneToDiseaseAssociation"],
            limit=10,
            offset=0
        )

@pytest.mark.asyncio
async def test_get_gene_expression_associations(mock_client):
    """Test gene to expression associations call."""
    gene_api = GeneApi()
    gene_id = "HGNC:1097"
    with patch.object(gene_api.entity_api, "get_associations", new_callable=AsyncMock) as mock_get_assoc:
        await gene_api.get_gene_expression_associations(mock_client, gene_id=gene_id, limit=15)
        mock_get_assoc.assert_called_once_with(
            mock_client,
            subject=[gene_id],
            category=["biolink:GeneToExpressionSiteAssociation"],
            limit=15,
            offset=0
        )