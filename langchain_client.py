import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()


async def main():
    print("hello lanchain mcp")
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/michael/projects/mcp-langchain-adapters/servers/math_server.py"
                ],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    )
    async with client.session("weather") as session:
        tools = await load_mcp_tools(session)
        agent = create_react_agent(
            model=llm,
            tools=tools,
        )
        # result = await agent.ainvoke({"messages": "What is 2 + 2?"})
        result = await agent.ainvoke(
            {"messages": "What is the weather in Boise, Idaho?"}
        )
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
