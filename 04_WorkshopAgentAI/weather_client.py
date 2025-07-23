from fastmcp import Client
import asyncio

async def main():
    async with Client("weather_server.py") as mcp_client:
        # Call 
        tools = await mcp_client.list_tools()
        print(f"Available tools: {tools}")

        # Call the 'get_weather' tool
        get_weather_result = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print(f"get_weather: {get_weather_result}")

if __name__ == "__main__":
    test = asyncio.run(main())
    #print(test)
