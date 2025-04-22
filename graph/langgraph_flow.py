from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from agents.research_agent import research_agent
from agents.answer_drafter_agent import answer_drafter

class State(TypedDict):
    query: str
    docs: List[str]
    final_answer: str

def research_node(state):
    docs = research_agent(state["query"])
    return {"docs": docs}

def answer_draft_node(state):
    answer = answer_drafter(state["docs"], state["query"])
    return {"final_answer": answer}

def run_graph(query: str):
    graph = StateGraph(State)

    # Define input and output for each node
    graph.add_node("research", research_node)
    graph.add_node("draft", answer_draft_node)

    graph.set_entry_point("research")
    graph.add_edge("research", "draft")
    graph.add_edge("draft", END)

    app = graph.compile()
    state = {"query": query}
    result = app.invoke(state)

    return result["final_answer"]
