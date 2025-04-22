# deep_research_ai/agents/answer_drafter_agent.py
import google.generativeai as genai
from langchain.schema import Document
import os
from datetime import datetime
import re

# Configure the Gemini API
GEMENI_API = os.getenv("GEMENI_API_KEY")
genai.configure(api_key= GEMENI_API)

def clean_markdown(text: str) -> str:
    # Remove markdown headers
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    
    # Remove bold and italic markers
    text = re.sub(r'\*\*|\*|__|_', '', text)
    
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    
    # Remove inline code
    text = re.sub(r'`', '', text)
    
    # Remove links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove horizontal rules
    text = re.sub(r'---|___|\*\*\*', '', text)
    
    # Remove blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    
    # Remove lists markers but keep the content
    text = re.sub(r'^[\s-]*[\d.]+\s*', '', text, flags=re.MULTILINE)
    
    # Clean up multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()

def save_answer_to_file(answer: str, query: str):
    # Create answers directory if it doesn't exist
    os.makedirs("answers", exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Clean query for filename
    clean_query = "".join(c for c in query if c.isalnum() or c in (' ', '-', '_')).strip()
    filename = f"answers/{timestamp}_{clean_query[:50]}.txt"
    
    # Save the answer
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Query: {query}\n\n")
        f.write("Answer:\n")
        f.write(answer)
    
    return filename

def answer_drafter(documents: list[Document], query: str) -> str:
    if not documents:
        return "No relevant data was found for this query."
    
    # Combine all document contents
    combined_content = "\n\n".join([doc.page_content for doc in documents])
    
    # Create the prompt with formatting instructions
    prompt = f"""Based on the following research information, provide a comprehensive and well-structured answer. 
Please format your response with these guidelines:
- Use bullet points (•) for key points
- Add relevant emojis to make the content more engaging
- Use clear section headers with emojis
- Keep the language professional but accessible
- Do not use any markdown symbols like #, *, or _
- Use proper spacing and indentation
- Make sections visually distinct

Research information:
{combined_content}

Please provide a detailed answer that synthesizes the information above, using the requested formatting."""
    
    # Generate the response
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    
    # Clean the response of any markdown
    answer = clean_markdown(response.text)
    
    # Save the answer to a file
    filename = save_answer_to_file(answer, query)
    print(f"\nAnswer saved to: {filename}")
    
    return answer
