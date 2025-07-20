from langchain.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()

def fetch_knowledge(state):
    query = state.get("parsed_question") or state["user_question"] #If "parsed_question" is missing or empty, it falls back to the original "user_question"
    result = search.run(query) #sends the query to DuckDuckGo and fetches search results. result is a string summary or concatenation of top search results returned by the tool
    state["external_facts"] = result[:500]  # Limit size
    return state
