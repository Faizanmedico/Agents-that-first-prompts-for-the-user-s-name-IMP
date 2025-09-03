# app.py
# This file contains the main application logic for running our agent.

from agents import Agent, Runner
# Import the model and config objects from our new connection file.
from connection import config, model

# Define the agent.
agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model # Use the model object from our connection file.
)

# Run the agent synchronously with a specific prompt.
result = Runner.run_sync(
    agent, 
    "Hello, how are you.", 
    run_config=config # Use the config object from our connection file.
)

# Print the final response from the agent.
print(result.final_output)
