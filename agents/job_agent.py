import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()
# SERVER
server_params = StdioServerParameters( command="python", args=["mcp_servers/search_server.py"], )


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # Load MCP tools
            tools = await load_mcp_tools(session)

            # Create LLM
            llm = ChatGroq(
                  model="llama-3.3-70b-versatile"
             )
            # Create agent
            agent = create_agent(
                model=llm,
                tools=tools
            )

            # Invoke agent
            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": "Find Prompt Engineer jobs in India and provide company, location and application link."
                        }
                    ]
                }
            )

            print(response)
    
if __name__ == "__main__":
    asyncio.run(main())