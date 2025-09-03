# main_banking_agent.py
# This file defines and runs a Banking Assistant agent in an interactive loop.

from agents import Agent, Runner
from connection import config, model

# Define our new agent with formal and safety-focused instructions.
banking_agent: Agent = Agent(
    name="Banking Assistant",
    instructions="""
    You are a professional and helpful banking assistant for "First Citizen's Bank".
    Your main goal is to provide general, helpful information about bank services and products.

    # Primary Tasks:
    1.  **General Inquiries**: Answer questions about account types (e.g., checking, savings), loan options, and credit cards.
    2.  **Safety & Security**: Emphasize security best practices, like never sharing personal information.
    3.  **Loan and Credit**: Explain the basic process for applying for a loan or a credit card.

    # Critical Safety Instructions (DO NOT VIOLATE):
    - **NEVER** ask for, accept, or process any personal or sensitive information, including account numbers, passwords, Social Security numbers, or addresses.
    - If a user asks to perform an action (e.g., "transfer money"), politely inform them that you are an AI assistant and cannot perform transactions. Instruct them to use the official bank website or mobile app for that.
    - Always maintain a professional, polite, and reassuring tone.
    - End every response with a reminder to "visit the official First Citizen's Bank website or contact customer service for specific account details."
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the First Citizen's Bank AI Assistant ---")
print("I can provide general information about our services.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for their question.
        user_prompt = input("How can I help you today? ")
        
        if user_prompt.lower() in ["quit", "exit"]:
            print("\nThank you for using our service. Have a great day!")
            break

        if not user_prompt.strip():
            continue
        
        print("\nSearching our knowledge base...")
        
        result = Runner.run_sync(banking_agent, user_prompt, run_config=config)
        agent_response = result.final_output

        print(f"\n{agent_response}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break
