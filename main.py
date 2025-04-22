# deep_research_ai/main.py
from graph.langgraph_flow import run_graph

def main():
    query = input("Enter your research query: ")
    final_output = run_graph(query)
    print("\nFinal Answer:\n", final_output)

if __name__ == "__main__":
    main()
