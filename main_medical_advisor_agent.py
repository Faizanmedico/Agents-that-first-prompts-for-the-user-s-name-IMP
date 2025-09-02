# main_medical_advisor_agent.py
# This file defines and runs a Medical Advisor Agent that collects user details before providing health advice.
from agents import Agent, Runner
from connection import config, model

# Define the MedicalAdvisorAgent.
medical_advisor_agent: Agent = Agent(
    name="MedicalAdvisorAgent",
    instructions="""
    You are a medical advisor. Provide information on common ailments, symptoms, and general health advice. 
    Emphasize that you are not a substitute for a professional medical diagnosis and users should consult a doctor.
    First, confirm the user's name and their health-related query (accept any input as valid for this simulation).
    Respond to the query with general advice in 1-2 sentences, ensuring clarity and professionalism.
    Include 'Consult a healthcare professional for personalized advice.' in each response, ending with #HealthTips.
    If the query is unclear, ask for clarification while maintaining professionalism.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the Medical Advisor Assistant! ---")
print("Please provide your name and health-related question.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Medical Advisor Assistant! #HealthTips")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get health-related question.
        health_query = input(f"Thank you, {user_name}. Please enter your health-related question: ")
        if health_query.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Medical Advisor Assistant! #HealthTips")
            break
        if not health_query.strip():
            print("Query cannot be empty. Please try again.")
            continue

        print("\nProcessing your health request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Health Query: {health_query}"
        result = Runner.run_sync(medical_advisor_agent, full_query, run_config=config)
        health_response = result.final_output
        print(f"\nHealth Advice: {health_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break