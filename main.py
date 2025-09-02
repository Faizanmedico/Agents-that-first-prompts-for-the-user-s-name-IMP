# main_bank_account_agent.py
# This file defines and runs a Bank Account Agent for First Citizen's Bank that collects user details before handling account queries.

from agents import Agent, Runner
from connection import config, model

# Define the BankAccountAgent.
bank_account_agent: Agent = Agent(
    name="BankAccountAgent",
    instructions="""
    You are a banking assistant for First Citizen's Bank, handling account information queries.
    First, confirm the user's name and account number (accept any input as valid for this simulation).
    Then, respond to the user's query by providing or modifying account information (e.g., balance, transactions, or updates) in 1-2 sentences.
    Include 'Member FDIC. Terms apply.' and 'For details: firstcitizens.com or 1-800-FCB-HELP' in each response, ending with #BankingBasics.
    If the query is unclear, ask for clarification while maintaining professionalism.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to First Citizen's Bank Account Assistant! ---")
print("Please provide your name, account number, and account-related question.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #BankingBasics")
            break

        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue
        
        # Step 2: Get account number.
        account_number = input(f"Thank you, {user_name}. Please enter your account number: ")
        
        if account_number.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #BankingBasics")
            break

        if not account_number.strip():
            print("Account number cannot be empty. Please try again.")
            continue
        
        # Step 3: Get account-related question.
        user_query = input("Your account-related question (e.g., check balance, update info): ")
        
        if user_query.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #BankingBasics")
            break

        if not user_query.strip():
            print("Query cannot be empty. Please try again.")
            continue
        
        print("\nProcessing your account request...")
        
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Account Number: {account_number}, Query: {user_query}"
        result = Runner.run_sync(bank_account_agent, full_query, run_config=config)
        account_response = result.final_output

        print(f"\nAccount Info: {account_response}\n")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break