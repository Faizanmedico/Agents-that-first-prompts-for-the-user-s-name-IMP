# main_small_business_consultant_agent.py
# This file defines and runs a Small Business Consultant Agent that collects user details before providing business advice.
from agents import Agent, Runner
from connection import config, model

# Define the SmallBusinessConsultantAgent.
small_business_consultant_agent: Agent = Agent(
    name="SmallBusinessConsultantAgent",
    instructions="""
    You are a small business consultant. Offer advice on starting, managing, or growing a business.
    First, confirm the user's name, business industry, and specific business-related query (accept any input as valid for this simulation).
    Respond to the query with tailored advice in 1-2 sentences, ensuring clarity and practicality.
    Include 'Consult a professional advisor for personalized business plans.' in each response, ending with #BusinessTips.
    If the query is unclear, ask for clarification while maintaining professionalism.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the Small Business Consultant Assistant! ---")
print("Please provide your name, business industry, and business-related question.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Small Business Consultant Assistant! #BusinessTips")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get business industry.
        business_industry = input(f"Thank you, {user_name}. Please enter your business industry (e.g., retail, tech): ")
        if business_industry.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Small Business Consultant Assistant! #BusinessTips")
            break
        if not business_industry.strip():
            print("Business industry cannot be empty. Please try again.")
            continue

        # Step 3: Get business-related question.
        business_query = input("Please enter your business-related question (e.g., marketing strategies, funding options): ")
        if business_query.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Small Business Consultant Assistant! #BusinessTips")
            break
        if not business_query.strip():
            print("Query cannot be empty. Please try again.")
            continue

        print("\nProcessing your business request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Business Industry: {business_industry}, Business Query: {business_query}"
        result = Runner.run_sync(small_business_consultant_agent, full_query, run_config=config)
        business_response = result.final_output
        print(f"\nBusiness Advice: {business_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break

        