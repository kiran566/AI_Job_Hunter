import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
# server in another file
# starts the server when need ed to connect to it
server_params = StdioServerParameters(
    command="python",
    args=["mcp_servers/search_server.py"],
)

# client session to connect to the server
async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()
            # with initialize, we can call the tool registered on the server
            # asking for toola avial
            tools = await session.list_tools()
            print("Available Tools:")

            for tool in tools.tools:
                print(tool.name)
            
            result = await session.call_tool(
    "search_jobs",
    {
        "role": "Prompt Engineer"
    }
        )
            
            print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())

 
