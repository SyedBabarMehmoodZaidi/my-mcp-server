from mcp.server.fastmcp import FastMCP
from my_tool.math_tool import plus_function, subtract_function

app = FastMCP(name="my_server", stateless_http=True)

@app.tool(name="tool_plus", description="Math plus function tool.", title="Plus Tool")
def plus(n1: int, n2: int) -> str:
    """A simple addition function tool."""
    return plus_function(n1, n2)

@app.tool(name="tool_subtract", description="Math subtract function tool.", title="Subtract Tool")
async def subtract(n1: int, n2: int) -> str:
    """A simple subtraction function tool."""
    return subtract_function(n1, n2)

mcp_app = app.streamable_http_app()
     

