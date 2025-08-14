from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="simple_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions."),
    instruction=("Answer questions using Google Search when needed. Always cite sources."),
    tools=[google_search]
)