from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from agents.agent_a_intent.agent import agent as agent_a
classify_and_retrieve_tool = AgentTool(agent_a, "classify_intent")


root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="The root agent responsible for orchestrating sub-agents in the RAG system.",
    instruction="""
    You are the root controller in a multi-agent RAG system.

    When a query is received:
    - Call `classify_and_retrieve_tool(query)`
    - Return the tool's response as-is.

    Do not answer the query yourself.
    """,
    tools=[classify_and_retrieve_tool],
)
