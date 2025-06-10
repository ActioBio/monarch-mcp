from .entity import ENTITY_TOOLS, EntityApi
from .disease import DISEASE_TOOLS, DiseaseApi
from .gene import GENE_TOOLS, GeneApi
from .phenotype import PHENOTYPE_TOOLS, PhenotypeApi
from .similarity import SIMILARITY_TOOLS, SimilarityApi
from .search import SEARCH_TOOLS, SearchApi

# Aggregate all tools
ALL_TOOLS = (
    ENTITY_TOOLS +
    DISEASE_TOOLS +
    GENE_TOOLS +
    PHENOTYPE_TOOLS +
    SIMILARITY_TOOLS +
    SEARCH_TOOLS
)

# Map tool names to API classes
API_CLASS_MAP = {
    **{tool.name: EntityApi for tool in ENTITY_TOOLS},
    **{tool.name: DiseaseApi for tool in DISEASE_TOOLS},
    **{tool.name: GeneApi for tool in GENE_TOOLS},
    **{tool.name: PhenotypeApi for tool in PHENOTYPE_TOOLS},
    **{tool.name: SimilarityApi for tool in SIMILARITY_TOOLS},
    **{tool.name: SearchApi for tool in SEARCH_TOOLS},
}

__all__ = [
    "ALL_TOOLS",
    "API_CLASS_MAP",
    "EntityApi",
    "DiseaseApi", 
    "GeneApi",
    "PhenotypeApi",
    "SimilarityApi",
    "SearchApi",
]