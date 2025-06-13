# Monarch MCP Server

A Model Context Protocol (MCP) server that exposes the Monarch Initiative API as a set of tools.

## Features

### Core Capabilities

- **Entity Search**: Query genes, diseases, phenotypes across 33 integrated biomedical resources
- **Phenotype Matching**: Find similar diseases using semantic similarity algorithms
- **Cross-Species Analysis**: Explore gene-phenotype-disease relationships across human and model organisms
- **Association Discovery**: Navigate connections between genes, diseases, phenotypes, chemicals, and variants
- **Clinical Diagnostics**: Support rare disease diagnosis through phenotype profile matching
- **Ontology Mapping**: Translate between different biomedical nomenclatures (OMIM, MONDO, HP, etc.)
- **Chemical/Drug Data**: Access drug-disease relationships and treatment information

### Data Sources

The Monarch Knowledge Graph integrates 33 biomedical resources:

- **Clinical/Genetics**: OMIM, Orphanet, ClinVar, HGNC, HPO (Human Phenotype Ontology)
- **Model Organisms**: Alliance of Genome Resources (MGI, ZFIN, WormBase, FlyBase, Xenbase, RGD), dictyBase, PomBase, SGD
- **Ontologies**: MONDO (diseases), Gene Ontology, Uberon (anatomy), CHEBI (chemicals), PHENIO (cross-species phenotypes)
- **Pathways & Interactions**: Reactome, STRING, BioGRID
- **Expression**: Bgee (gene expression across species)
- **Proteins**: UniProt
- **Literature**: PubMed annotations
- **Reference**: Ensembl, NCBI Gene

## Quick Start

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Setup**
   ```bash
   cd monarch-mcp
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

3. **Configure Claude Desktop**
   ```bash
   python scripts/configure_claude.py
   ```
   Then restart Claude Desktop.

## Usage

#### Running the Server

```bash
monarch-mcp
```

#### AI Agent Example

```bash
# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run the example agent
python examples/react_agent.py
```

#### Development

```bash
# Run tests
pytest tests/ -v
```
