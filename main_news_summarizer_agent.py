# main_news_summarizer_agent.py
# This file defines and runs a News Summarizer Agent that collects user details and summarizes news articles.
from agents import Agent, Runner
from connection import config, model

# Define the NewsSummarizerAgent.
news_summarizer_agent: Agent = Agent(
    name="NewsSummarizerAgent",
    instructions="""
    You are a news summarizer. Provide concise summaries of current events or breaking news from provided article URLs or text.
    First, confirm the user's name and the news article URL or pasted text (accept any input as valid for this simulation).
    If a URL is provided, summarize the key points of the article in 1-2 sentences, focusing on the main event, involved parties, and implications.
    If text is provided, summarize it similarly. If the input is unclear or inaccessible (e.g., paywalled URL), ask for clarification or suggest pasting the text.
    Include 'Source the original article for full details.' in each response, ending with #NewsBite.
    Maintain objectivity and neutrality in all summaries.
    """,
    model=model
)

# Start the interactive session.
print("--- Welcome to the News Summarizer Assistant! ---")
print("Please provide your name and a news article URL or pasted text to summarize.")
print("Type 'quit' or 'exit' at any step to end the session.\n")

while True:
    try:
        # Step 1: Get user's name.
        user_name = input("Please enter your full name: ")
        if user_name.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the News Summarizer Assistant! #NewsBite")
            break
        if not user_name.strip():
            print("Name cannot be empty. Please try again.")
            continue

        # Step 2: Get news article URL or text.
        news_input = input(f"Thank you, {user_name}. Please enter a news article URL or paste the article text: ")
        if news_input.lower() in ["quit", "exit"]:
            print("\nGoodbye! Thank you for using the News Summarizer Assistant! #NewsBite")
            break
        if not news_input.strip():
            print("Article URL or text cannot be empty. Please try again.")
            continue

        print("\nProcessing your news summary request...")
        # Combine inputs for the agent to process.
        full_query = f"Name: {user_name}, News Input: {news_input}"
        result = Runner.run_sync(news_summarizer_agent, full_query, run_config=config)
        summary_response = result.final_output
        print(f"\nNews Summary: {summary_response}\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break

        