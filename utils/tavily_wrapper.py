# deep_research_ai/utils/tavily_wrapper.py
from tavily import TavilyClient
import os
TAVILY_API = os.getenv("TAVILY_API_KEY")
# To install: pip install tavily-python
def tavily_search(query: str):
    client = TavilyClient(api_key= TAVILY_API)
    response = client.search(query=query, search_depth="advanced", include_answer=False)
    print("Tavily response:", response)  # Debug print
    return response.get("results", [])
