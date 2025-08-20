import os
import time
from functools import lru_cache

import httpx
from fastmcp import FastMCP

TTL = 6 * 60 * 60  # 6 hours in seconds
TANKARTA_URL = os.getenv("TANKARTA_URL")
mcp = FastMCP(
    "🚀 Orlen Tankarta ⛽",
    instructions="""
    This MCP server provides tools to get current discounted Orlen Tankarta Business price of fuel.
    """,
)


@lru_cache(maxsize=None)
def cached_price() -> tuple[str, float]:
    """Get current discounted price of fuel."""
    response = httpx.get(TANKARTA_URL)
    return response.content.decode("utf-8"), time.time()


@mcp.tool
def price() -> str:
    """Get current discounted price of fuel."""
    price, ts = cached_price()
    if time.time() - ts > TTL:
        cached_price.cache_clear()
        price, _ = cached_price()
    return price


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
