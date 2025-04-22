# deep_research_ai/utils/document_utils.py
from langchain.schema import Document

def create_documents(results):
    documents = []
    for item in results:
        content = item.get("content", "")
        source = item.get("url", "unknown")
        if content:
            documents.append(Document(page_content=content, metadata={"source": source}))
    return documents
