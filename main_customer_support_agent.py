# main_customer_support_agent.py
# This file defines and runs a Customized AI Customer Support Agent for First Citizen's Bank that collects user details and handles customer support queries.
from agents import Agent, Runner
from connection import config, model

# Define the CustomerSupportAgent.
customer_support_agent: Agent = Agent(
    name="CustomerSupportAgent",
    instructions="""
    You are an AI-powered customer support agent for First Citizen's Bank, handling inquiries with professionalism and empathy in 2025.
    First, confirm the user's name, customer ID (accept any input as valid for this simulation), and support query.
    Analyze the query for sentiment to prioritize urgent or negative issues (e.g., complaints) and respond in 1-2 sentences with clear, actionable solutions or escalations.
    Use a friendly tone, offer practical advice (e.g., troubleshooting, branch visits, or contact options), and ensure responses align with banking services like accounts, loans, or online banking.
    Include 'Member FDIC. Terms apply. Contact us at firstcitizens.com or 1-800-FCB-HELP for further assistance.' in each response, ending with #CustomerFirst.
    If the query is unclear, ask for clarification while maintaining a supportive tone.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to First Citizen's Bank Customer Support Assistant! ---")
print("We're here to assist with your banking needs in 2025.")
print("Please provide your name, customer ID, and support query.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #CustomerFirst")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get customer ID.
        customer_id = input(f"Thank you, {user_name}. Please enter your customer ID: ")
        if customer_id.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #CustomerFirst")
            break
        if not customer_id.strip():
            print("Customer ID cannot be empty. Please try again.")
            continue

        # Step 3: Get support query.
        support_query = input("Please enter your support query (e.g., account access issue, loan inquiry): ")
        if support_query.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing First Citizen's Bank! #CustomerFirst")
            break
        if not support_query.strip():
            print("Query cannot be empty. Please try again.")
            continue

        print("\nProcessing your support request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Customer ID: {customer_id}, Support Query: {support_query}"
        result = Runner.run_sync(customer_support_agent, full_query, run_config=config)
        support_response = result.final_output
        print(f"\nSupport Response: {support_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break