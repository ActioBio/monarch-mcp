# Monarch MCP Server

A Model Context Protocol (MCP) server that exposes the Monarch Initiative API as a set of tools.

### Quick Start

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Setup**
   ```bash
   git clone https://github.com/nickzren/monarch-mcp.git
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