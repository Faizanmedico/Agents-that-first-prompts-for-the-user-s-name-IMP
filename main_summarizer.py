# main_summarizer.py
# This file defines and runs an interactive agent that summarizes restaurant reviews.

# We reuse the same connection settings.
from agents import Agent, Runner
from connection import config, model

# Define our new agent with instructions to be a review summarizer.
# This is a more complex instruction set to handle the specific task.
summarizer_agent: Agent = Agent(
    name="ReviewSummarizer",
    instructions="You are an expert at summarizing customer reviews for a restaurant. Your task is to read a review and summarize the main positive and negative points in a concise, bullet-point format. Do not add any extra commentary, just the summary.",
    model=model
)

# Use a loop for an interactive summarization experience.
print("--- Welcome to the Restaurant Review Summarizer ---")
print("Paste a restaurant review and I will summarize it for you.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        # Get user input for the review text.
        review_text = input("Paste a review: ")
        
        # Exit the loop if the user types 'quit' or 'exit'.
        if review_text.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break

        # Check for empty input.
        if not review_text.strip():
            continue

        # Run the agent with the text to summarize.
        print("\nSummarizing...")
        result = Runner.run_sync(summarizer_agent, review_text, run_config=config)
        summary = result.final_output

        # Print the summary.
        print(f"Summary:\n{summary}\n")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

