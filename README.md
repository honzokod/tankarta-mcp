# Tankarta MCP
MCP server to get current discounted fuel prices.
It depends on [skateman's tankarta implementation](https://github.com/skateman/nexus/blob/master/src/functions/tankarta.js).

Install the project with `uv`:
```bash
uv tool install .
```
and run the server with:
```bash
export TANKARTA_URL="<your skateman tankarta endpoint url>"
uvx tankarta-mcp
```
## Integration
### Cursor
To set it up with Cursor, use [mcp.json](mcp.json), set the TANKARTA_URL environment variable, and copy it to `~/.cursor/mcp.json`.

### Open WebUI
A container image is available that runs tankarta-mcp with [mcpo](https://github.com/open-webui/mcpo) so it can be integrated with [Open WebUI](https://github.com/open-webui/open-webui).
Run the image usign
```bash
docker run --rm -p 8000:8000 --env TANKARTA_URL=<url> ghcr.io/honzokod/tankarta-mcpo:latest
```
