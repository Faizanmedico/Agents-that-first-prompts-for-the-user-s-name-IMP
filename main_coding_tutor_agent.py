# main_coding_tutor_agent.py
# This file defines and runs a Coding Tutor Agent that assists users with programming concepts, debugging, and explanations.
from agents import Agent, Runner
from connection import config, model

# Define the CodingTutorAgent.
coding_tutor_agent: Agent = Agent(
    name="CodingTutorAgent",
    instructions="""
    You are a coding tutor. Teach programming concepts, debug code, and explain languages like Python or JavaScript.
    First, confirm the user's name, skill level (e.g., beginner, intermediate, advanced), and project goals (e.g., learning basics, building a project, debugging code).
    Accept any input as valid for this simulation.
    If the user provides code, analyze it, suggest fixes, or explain its functionality clearly.
    If the user asks about a concept, provide a concise explanation tailored to their skill level.
    If the input is unclear, ask for clarification (e.g., specific language, code snippet, or topic).
    End each response with '#CodeMentor' to mark it as a tutoring session.
    Maintain a patient, encouraging, and clear tone in all responses.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the Coding Tutor Assistant! ---")
print("Please provide your name, skill level, and project goals to get tailored coding help.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Coding Tutor Assistant! #CodeMentor")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get user's skill level.
        skill_level = input(f"Thank you, {user_name}. Please enter your programming skill level (e.g., beginner, intermediate, advanced): ")
        if skill_level.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Coding Tutor Assistant! #CodeMentor")
            break
        if not skill_level.strip():
            print("Skill level cannot be empty. Please try again.")
            continue

        # Step 3: Get user's project goals or coding query.
        coding_input = input(f"Great, {user_name}. Please describe your project goals or share a coding question/code snippet: ")
        if coding_input.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the Coding Tutor Assistant! #CodeMentor")
            break
        if not coding_input.strip():
            print("Project goals or coding question cannot be empty. Please try again.")
            continue

        print("\nProcessing your coding tutor request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, Skill Level: {skill_level}, Coding Input: {coding_input}"
        result = Runner.run_sync(coding_tutor_agent, full_query, run_config=config)
        tutor_response = result.final_output
        print(f"\nCoding Tutor Response: {tutor_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break