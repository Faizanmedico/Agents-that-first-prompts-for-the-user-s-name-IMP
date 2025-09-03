# main_fact_agent.py
# This file contains the logic for our new Fact Generator Agent.

import asyncio
from agents import Agent, Runner
from connection import config, model

# Define the agent with new, simple instructions.
fact_agent = Agent(
    name="Fact Generator",
    instructions="You are a helpful assistant that provides a single, interesting fact about the topic provided by the user.",
    model=model
)

async def main():
    print("--- Welcome to the Fact Generator! ---")
    print("I'm here to give you an interesting fact about any topic you choose.")
    print("Type 'quit' or 'exit' to end the session.")
    
    while True:
        user_input = input("\nTopic: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        
        print("\nSearching for a fascinating fact...")
        
        # Run the agent with the user's input as the prompt.
        result = await Runner.run(
            fact_agent,
            f"Provide an interesting fact about {user_input}",
            run_config=config
        )
        
        # Print the agent's response.
        print(f"\nFact: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
