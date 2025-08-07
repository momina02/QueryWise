import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, AIMessage

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

chat = ChatGroq(
    groq_api_key=groq_key,
    model_name="llama3-70b-8192"
)

# History for chat
chat_history = []

def generate_augmented_prompt(query, docs):
    context = "\n".join([doc.page_content for doc in docs])
    return f"""Using the context below, answer the question.

Context:
{context}

Question: {query}"""


def chat_with_docs(query, vectorstore):
    # Try to retrieve documents
    docs = vectorstore.similarity_search(query, k=3)
    
    if docs:
        # Use RAG (with context from docs)
        prompt = generate_augmented_prompt(query, docs)
    else:
        # Use query directly — LLM will answer from its own knowledge
        prompt = query

    # Update chat history
    chat_history.append(HumanMessage(content=prompt))
    response = chat(chat_history)
    chat_history.append(AIMessage(content=response.content))
    return response.content

