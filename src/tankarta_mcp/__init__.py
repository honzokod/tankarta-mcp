import os
import httpx
from fastmcp import FastMCP


TANKARTA_URL = os.getenv("TANKARTA_URL")
mcp = FastMCP(
    "🚀 Orlen Tankarta ⛽",
    instructions="""
    This MCP server provides tools to get current discounted Orlen Tankarta Business price of fuel.
    """
)


@mcp.tool
def price() -> int:
    """Get current discounted price of fuel."""
    response = httpx.get(TANKARTA_URL)
    return response.content.decode("utf-8")

def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()
