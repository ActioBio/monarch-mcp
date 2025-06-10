# Monarch MCP Server

A Model Context Protocol (MCP) server that exposes the Monarch Initiative API as a set of tools.

## Installation

```bash
git clone https://github.com/nickzren/monarch-mcp
cd monarch-mcp
mamba env create -f environment.yml
mamba activate monarch-mcp
```

## Usage

#### As an MCP Server

```bash
monarch-mcp
```

#### Configure with Claude Desktop

```bash
python scripts/configure_claude.py
```

## Example

#### Interactive ReAct Agent

The repository includes an example agent that demonstrates how to use the query library to build intelligent applications.

1.  Set your API credentials: Create or update a .env file in the project root:
    ```bash
    echo "OPENAI_MODEL=gpt-4.1-mini" > .env
    echo "OPENAI_API_KEY=YOUR_API_KEY" >> .env
    ```

2.  Run the agent:
    ```bash
    python examples/react_agent.py

    --- Open Targets ReAct Agent ---
    Ask a complex question. Type 'exit' to quit.

    > Find targets for metatropic dysplasia and see if TRPV4 is one of them.
    ```