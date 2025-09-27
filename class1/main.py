from mcp.server.fastmcp import FastMCP

app = FastMCP(name="my_server", stateless_http=True)

@app.tool()
def plus(n1: int, n2: int) -> str:
    """A simple addition function tool."""
    return f"your answer is{n1 + n2}"

mcp_app = app.streamable_http_app()


