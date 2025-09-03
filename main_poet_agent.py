# This script is a template for a new agent.

# The import statement has been corrected to import the 'config' and 'model'
# variables from conection.py.
from agents import Agent, Runner
from connection import config, model

# Here you would define your new agent.
# For example, let's create a "Poet" agent.
poet_agent: Agent = Agent(
    name="Poet",
    instructions="You are a brilliant poet. Your goal is to write a short, beautiful poem based on a user's prompt.",
    model=model
)

# You can define a new user prompt.
user_prompt = "Write a poem about the sunrise."

# Run the agent with your new prompt.
result = Runner.run_sync(poet_agent, user_prompt, run_config=config)

# Print the final output from the agent's run.
print(f"--- The Poet's Creation ---\n\n{result.final_output}")

