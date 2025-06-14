from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Import the tool from Agent A
from agents.agent_a_intent.agent import agent as agent_a

# Wrap classify_intent from Agent A as a callable tool
classify_intent_tool = AgentTool(agent_a, "classify_intent")

# Define root agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="The root agent responsible for orchestrating sub-agents in the RAG system.",
    instruction="""
    You are the root controller agent in a multi-agent RAG system.

    Your task is to receive the user query and determine whether it can be answered using the PDF vector database.
    To do this, you must call the `classify_intent_tool`, which is part of the `agent_a_intent` agent.


    Return the result from `classify_intent_tool` exactly as received. Do not paraphrase or modify the structure.

    Do not attempt to classify the query yourself. Always delegate this task to the intent classification tool.
    """,
    tools=[classify_intent_tool],
)
