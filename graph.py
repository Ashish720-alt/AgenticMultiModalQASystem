from langgraph.graph import StateGraph, END
from state import GraphSharedState

from agents.vision_agent import analyze_image
from agents.question_agent import parse_question
from agents.knowledge_agent import fetch_knowledge
from agents.answer_agent import generate_answer


# Create a new graph
graph = StateGraph(GraphSharedState)

# Add each node in the agent workflow
graph.add_node("vision_analysis", analyze_image)
graph.add_node("question_parser", parse_question)
graph.add_node("knowledge_lookup", fetch_knowledge)
graph.add_node("answer_generator", generate_answer)

# Connect the nodes sequentially - in LangGraph each function has the same argument which is GraphSharedState i.e. a dictionary
graph.set_entry_point("vision_analysis")                  # First step: vision agent
graph.add_edge("vision_analysis", "question_parser")      # Then parse the question
graph.add_edge("question_parser", "knowledge_lookup")     # Then fetch facts
graph.add_edge("knowledge_lookup", "answer_generator")    # Then generate the answer
graph.add_edge("answer_generator", END)                   # End of workflow

# Compile into an executable graph app
app = graph.compile()