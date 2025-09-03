# main_compliment_agent.py
# This file defines and runs a simple Compliment Generator agent.

from agents import Agent, Runner
from connection import config, model

# Define our new agent with very simple, positive instructions.
compliment_agent: Agent = Agent(
    name="ComplimentGenerator",
    instructions="""
    You are a cheerful and encouraging assistant whose sole purpose is to generate positive and uplifting compliments.
    When the user provides a name or a general topic, respond with a unique and heartfelt compliment.
    Keep your compliments concise and genuine.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the Compliment Generator! ---")
print("I'm here to brighten your day with a compliment.")
print("Tell me your name, or a general topic for a compliment. Type 'quit' or 'exit' to end.\n")

while True:
    try:
        # Get user input.
        user_input = input("What or who should I compliment? ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("\nGoodbye! Remember, you're amazing!")
            break

        if not user_input.strip():
            continue
        
        print("\nThinking of something nice to say...")
        
        result = Runner.run_sync(compliment_agent, user_input, run_config=config)
        agent_response = result.final_output

        print(f"\n{agent_response}\n")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break

