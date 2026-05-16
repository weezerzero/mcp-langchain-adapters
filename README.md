# mcp-langchain-adapters

Small experimental workspace for **Model Context Protocol (MCP)** servers and wiring them to **LangChain** using [`langchain-mcp-adapters`](https://pypi.org/project/langchain-mcp-adapters/). The goal is to stand up simple MCP tools locally, then plug them into LangChain agents or LangGraph flows.

## Requirements

- **Python 3.14+** (see `requires-python` in `pyproject.toml`)
- [**uv**](https://docs.astral.sh/uv/) (recommended) or another PEP 517 installer

## Setup

```bash
git clone <repository-url>
cd mcp-langchain-adapters
uv sync
```

Create a `.env` file in the project root (this file is gitignored). At minimum you’ll need an OpenAI API key if you call OpenAI-backed models from LangChain:

```bash
OPENAI_API_KEY=your-key-here
```

Optional LangSmith tracing (only if you use it):

```bash
LANGCHAIN_API_KEY=your-langsmith-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=mcp-langchain-adapters
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

## Project layout

| Path | Purpose |
|------|---------|
| `main.py` | Async entrypoint (placeholder; extend here to build agents/graphs that use MCP tools). |
| `servers/math_server.py` | Example MCP server with `add` and `multiply` tools (**stdio** transport). |
| `servers/weather_server.py` | Example MCP server with a demo `get_weather` tool (**SSE** transport). |

Dependencies are declared in `pyproject.toml`; `mcp` is pulled in via `langchain-mcp-adapters`.

## Running the MCP servers

From the repository root:

**Math server (stdio)** — typical for subprocess / IDE MCP clients:

```bash
uv run python servers/math_server.py
```

**Weather server (SSE)** — listens with Server-Sent Events; point your MCP client at the URL the server prints when it starts:

```bash
uv run python servers/weather_server.py
```

## Next steps

- Use `langchain-mcp-adapters` in `main.py` to load these servers as LangChain tools and attach them to a chat model or LangGraph.
- Add more servers under `servers/` following the same FastMCP patterns.
