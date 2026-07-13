import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
from database.db import save_job, get_jobs

mcp = FastMCP("Database Server")


@mcp.tool()
def save_job_tool(
    title: str,
    company: str,
    location: str,
    url: str,
):
    """
    Save a job into the database.
    """
    return save_job(
        title,
        company,
        location,
        url
    )


@mcp.tool()
def get_saved_jobs():
    """
    Return all saved jobs.
    """
    return get_jobs()


if __name__ == "__main__":
    mcp.run()