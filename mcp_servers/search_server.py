from mcp.server.fastmcp import FastMCP
# creating a new instance of FastMCP with the name "Job Search Server"

mcp = FastMCP("Job Search Server")
# registering n tool on this server
@mcp.tool()
def search_jobs(role: str):
    """
    Search jobs by role.
    """

    return [
        {
            "title": "Prompt Engineer",
            "company": "ABC AI",
            "location": "Hyderabad"
        },
        {
            "title": "LLM Engineer",
            "company": "XYZ",
            "location": "Bangalore"
        }
    ]

if __name__ == "__main__":
    mcp.run()