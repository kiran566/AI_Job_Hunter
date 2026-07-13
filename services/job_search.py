# search logic for the job search server
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_jobs(role: str):

    query = f"""
    Latest {role} jobs in India.
    Include company, location and application link.
    """

    result = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return result["results"]
# so that we can change tavily any other job search platform in future without changing the server code, we are using this adapter pattern