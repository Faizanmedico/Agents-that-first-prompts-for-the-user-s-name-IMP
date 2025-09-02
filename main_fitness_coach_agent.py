# main_fitness_coach_agent.py
# This file defines and runs a Fitness Coach Agent that collects user details before providing fitness advice.
from agents import Agent, Runner
from connection import config, model

# Define the FitnessCoachAgent.
fitness_coach_agent: Agent = Agent(
    name="FitnessCoachAgent",
    instructions="""
    You are a fitness coach. Offer personalized workout routines, nutrition tips, and motivational support.
    First, confirm the user's name, fitness goals, and current fitness level (accept any input as valid for this simulation).
    Respond to the query with tailored advice in 1-2 sentences, ensuring clarity and encouragement.
    Include 'Stay consistent and consult a professional for personalized plans.' in each response, ending with #FitnessMotivation.
    If the query is unclear, ask for clarification while maintaining professionalism.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the Fitness Coach Assistant! ---")
print("Please provide your name, fitness goals, and current fitness level.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing the Fitness Coach Assistant! #FitnessMotivation")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get fitness goals.
        fitness_goals = input(f"Thank you, {user_name}. Please enter your fitness goals (e.g., weight loss, muscle gain): ")
        if fitness_goals.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing the Fitness Coach Assistant! #FitnessMotivation")
            break
        if not fitness_goals.strip():
            print("Fitness goals cannot be empty. Please try again.")
            continue

        # Step 3: Get current fitness level.
        fitness_level = input("Please enter your current fitness level (e.g., beginner, intermediate): ")
        if fitness_level.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for choosing the Fitness Coach Assistant! #FitnessMotivation")
            break
        if not fitness_level.strip():
            print("Fitness level cannot be empty. Please try again.")
            continue

        print("\nProcessing your fitness request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Fitness Goals: {fitness_goals}, Fitness Level: {fitness_level}"
        result = Runner.run_sync(fitness_coach_agent, full_query, run_config=config)
        fitness_response = result.final_output
        print(f"\nFitness Advice: {fitness_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break


        