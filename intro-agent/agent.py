from google.adk.agents import Agent

root_agent = Agent(
    name="simple_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions."),
    instruction=("You are a helpful agent who can answer user questions."),
)
