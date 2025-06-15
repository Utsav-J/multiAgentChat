from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .classify_intent import classify_intent

agent = Agent(
    name="agent_a_intent",
    model="gemini-2.0-flash",
    description="Classifies user intent and optionally retrieves chunks from the vector DB.",
    instruction="""
    You are an intent classification agent in a multi-agent RAG system.

    1. Call `classify_intent(query)` to determine if the query can be answered using the PDF vector DB.
    2. If `can_answer_from_pdf` is true, call `retrieve_chunks_tool(query)` to retrieve top-k relevant chunks.
    3. Return a combined JSON object like:

    {
    "intent_classification": <result from classify_intent>,
    "retrieved_chunks": <result from retrieve_chunks_tool>
    }

    Only call the tools, do not answer queries yourself.
    """,
    tools=[classify_intent],
)
