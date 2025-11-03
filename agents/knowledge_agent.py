# agents/knowledge_agent.py
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_community")

from langchain_community.tools import DuckDuckGoSearchRun

# Simple search-based knowledge retriever
search = DuckDuckGoSearchRun()

def fetch_knowledge(query: str) -> str:
    """
    Fetches background knowledge from DuckDuckGo search.
    """
    try:
        return search.run(query)
    except Exception as e:
        return f"[Knowledge Agent Error] {e}"
