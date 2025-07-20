from langchain.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()

def fetch_knowledge(state):
    query = state.get("parsed_question") or state["user_question"]
    result = search.run(query)
    state["external_facts"] = result[:500]  # Limit size
    return state
