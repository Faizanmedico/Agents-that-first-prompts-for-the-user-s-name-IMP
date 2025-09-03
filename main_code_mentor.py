# main_code_mentor.py
# This file defines and runs a Code Mentor agent in an interactive loop.

from agents import Agent, Runner
from connection import config, model

# The instructions are excellent and will be kept as they are.
code_mentor_agent = Agent(
    name="Code Mentor",
    instructions="""
    # Modes:
    1. **Debugging Help**:
        - Ask for error logs/code snippets first.
        - Explain bugs in plain English + fix with inline comments.
    2. **Teaching Concepts** (e.g., "Explain recursion"):
        - Use analogies (e.g., "Russian dolls").
        - Provide 1 simple + 1 advanced example.
    3. **Code Review**:
        - Highlight 2 strengths + 2 improvements.
        - Enforce PEP-8/style guides.

    # Defaults:
    - Adapt to skill level (beginner/expert).
    - End with: "Try modifying [X] and see what happens!"
    """,
    model=model
)

# Start an interactive session to allow for a conversation.
print("--- Welcome to your interactive Code Mentor ---")
print("I'm ready to help you debug, learn, or review code.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input. This allows for a conversation.
        user_prompt = input("Your question or code: ")
        
        if user_prompt.lower() in ["quit", "exit"]:
            print("\nGoodbye! Happy coding.")
            break

        if not user_prompt.strip():
            continue
        
        print("\nThinking...")
        
        # We run the agent with the user's dynamic input.
        result = Runner.run_sync(code_mentor_agent, user_prompt, run_config=config)
        agent_response = result.final_output

        print(f"\n{agent_response}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

