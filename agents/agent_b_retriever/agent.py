from google.adk.agents import Agent
from .retrieve_chunks import retrieve_chunks

agent = Agent(
    name="agent_b_retriever",
    model="gemini-2.0-flash",  # Or the model you're using
    description="Retrieves the top-k most relevant chunks from the FAISS vector database based on a user query.",
    instruction="""
    You are a retrieval agent in a multi-agent RAG system.

    Your task is to take a user's query and retrieve the most relevant document chunks from the FAISS vector database.

    Use the `retrieve_chunks` tool to perform a similarity search. It will return a structured list of the top-k matching document chunks.

    Each chunk returned will contain:
    - `text`: The actual content from the document
    - `source`: The source or origin of the chunk (e.g., filename or document ID)
    - `page` : The page number where the content is located

    Always call the `retrieve_chunks` tool with the user's query and return the output exactly as provided by the tool.
    """,
    tools=[retrieve_chunks],
)
