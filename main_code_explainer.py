# main_code_explainer.py
# This file defines an agent that explains code and makes it interactive.

# We still reuse the connection settings.
from agents import Agent, Runner
from connection import config, model

# Define our new agent with a new set of instructions.
code_explainer_agent: Agent = Agent(
    name="CodeExplainer",
    instructions="You are a helpful programming assistant. Your goal is to explain code snippets in simple, clear language. Use Markdown for formatting code and key terms. If the user asks a question not related to code, kindly inform them you are an expert in code explanation.",
    model=model
)

# Use a loop to create an interactive chat experience.
# The user can type in their code snippet or question.
print("Welcome to the Code Explainer. Type 'quit' or 'exit' to end the session.")
while True:
    # Get user input from the command line.
    user_prompt = input("\nEnter a code snippet or question: ")
    
    # Exit the loop if the user types 'quit' or 'exit'.
    if user_prompt.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # Run the agent with the user's interactive prompt.
    print("\nProcessing...")
    result = Runner.run_sync(code_explainer_agent, user_prompt, run_config=config)

    # Print the agent's explanation.
    print(f"\n--- Code Explainer's Explanation ---\n{result.final_output}\n")

