
# Step 1 : Launch a MCP server
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("MCP-count-total-rs")

# Step 2 : Expose tools

@mcp.tool()

def count_total_rs(text: str) -> int:
    """Count the total number of Rs in the given string
    Input:
        text: str -> text to count the total number of Rs
    Output:
        count: int -> total number of Rs in the given string
    """

    if not isinstance(text,str):
        raise ValueError("text must be a string")
    
    return text.lower().count("r")


if __name__ == "__main__" :

    print("Starting MCP server at")
    mcp.run()