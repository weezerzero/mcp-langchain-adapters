import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
llm = OpenAIChat(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
stdio_server_params = StdioServerParams(
    command="python",
    args=["/Users/michael/projects/mcp-langchain-adapters/servers/math_server.py"]
)


async def main():
    print("Hello from mcp-langchain-adapters!")


if __name__ == "__main__":
    asyncio.run(main())
