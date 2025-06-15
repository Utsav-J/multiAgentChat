from google.adk.agents import Agent
from .generate_response import generate_response

agent = Agent(
    name="agent_c_llm",
    model="gemini-2.0-flash",
    description="Generates final LLM-based answer from retrieved chunks.",
    instruction="""
    You are the final answer generation agent in the RAG pipeline.

    Given a user query and a list of relevant content chunks from documents,
    call `generate_response(query, chunks)` to generate a clean, readable response.

    Do NOT answer on your own. Always use the tool.
    """,
    tools=[generate_response],
)
