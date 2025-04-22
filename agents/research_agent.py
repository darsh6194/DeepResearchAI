# deep_research_ai/agents/research_agent.py
from utils.tavily_wrapper import tavily_search
from utils.document_utils import create_documents

def research_agent(query: str):
    results = tavily_search(query)
    return create_documents(results)
