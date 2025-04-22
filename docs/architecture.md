# Deep Research AI Architecture

## System Overview

```mermaid
graph TD
    A[User Query] --> B[Flask Web Interface]
    B --> C[LangGraph Workflow]
    C --> D[Research Agent]
    D --> E[Tavily Search]
    E --> F[Document Processing]
    F --> G[Answer Drafter]
    G --> H[Gemini AI]
    H --> I[Formatted Answer]
    I --> J[Save to File]
    I --> K[Display to User]

    subgraph "LangGraph Components"
        C
        D
        F
        G
    end

    subgraph "LangChain Components"
        E
        F
        G
    end
```

## Component Details

### LangGraph Implementation
```python
# State Definition
class State(TypedDict):
    query: str
    docs: List[str]
    final_answer: str

# Graph Construction
graph = StateGraph(State)
graph.add_node("research", research_node)
graph.add_node("draft", answer_draft_node)
```

### LangChain Integration
- Document Processing
- Research Agent
- Answer Generation
- State Management

## Flow Description

1. **User Input**
   - Query entered through web interface
   - Sent to LangGraph workflow

2. **Research Phase**
   - LangGraph triggers research agent
   - Tavily search performed
   - Documents processed using LangChain

3. **Answer Generation**
   - Documents passed to answer drafter
   - Gemini AI generates formatted response
   - Answer saved and displayed

4. **Output**
   - Formatted answer with bullet points and emojis
   - Saved to file
   - Displayed to user 