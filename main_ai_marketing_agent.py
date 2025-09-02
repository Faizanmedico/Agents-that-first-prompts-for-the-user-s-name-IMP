# main_ai_marketing_agent.py
# This file defines and runs an AI Marketing Agent that collects user details before providing innovative marketing strategies, inspired by 2025 AI trends.
from agents import Agent, Runner
from connection import config, model

# Define the AIMarketingAgent.
ai_marketing_agent: Agent = Agent(
    name="AIMarketingAgent",
    instructions="""
    You are an AI-powered marketing agent specializing in cutting-edge strategies for small businesses in 2025. 
    Leverage trends like autonomous AI agents, personalization, and e-commerce automation to provide innovative, actionable advice.
    First, confirm the user's name, business industry, and specific marketing-related query (accept any input as valid for this simulation).
    Respond with a tailored marketing strategy in 2-3 sentences, including creative ideas like AI-driven content creation, viral social campaigns, or targeted ads.
    Make it surprising and forward-thinking, incorporating elements like AI agents for lead gen or real-time personalization.
    Include 'Adapt these ideas to your needs and consult experts for implementation.' in each response, ending with #AIMarketing2025.
    If the query is unclear, ask for clarification while maintaining enthusiasm and professionalism.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the AI Marketing Agent Assistant! ---")
print("Discover cutting-edge marketing strategies powered by 2025 AI trends.")
print("Please provide your name, business industry, and marketing-related question.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the AI Marketing Agent Assistant! #AIMarketing2025")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get business industry.
        business_industry = input(f"Thank you, {user_name}. Please enter your business industry (e.g., tech, retail): ")
        if business_industry.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the AI Marketing Agent Assistant! #AIMarketing2025")
            break
        if not business_industry.strip():
            print("Business industry cannot be empty. Please try again.")
            continue

        # Step 3: Get marketing-related question.
        marketing_query = input("Please enter your marketing-related question (e.g., how to go viral, AI ad optimization): ")
        if marketing_query.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the AI Marketing Agent Assistant! #AIMarketing2025")
            break
        if not marketing_query.strip():
            print("Query cannot be empty. Please try again.")
            continue

        print("\nProcessing your marketing strategy request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Business Industry: {business_industry}, Marketing Query: {marketing_query}"
        result = Runner.run_sync(ai_marketing_agent, full_query, run_config=config)
        marketing_response = result.final_output
        print(f"\nAI Marketing Strategy: {marketing_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break


        