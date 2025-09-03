# main_translator.py
# This file defines and runs an interactive agent that translates English to Urdu.
# It now includes functionality to save and display a translation history.

import json
import os

from agents import Agent, Runner
from connection import config, model

# Define the filename for our translation history.
TRANSLATION_HISTORY_FILE = "translation_history.json"

def load_history():
    """Loads the translation history from a JSON file."""
    if os.path.exists(TRANSLATION_HISTORY_FILE):
        with open(TRANSLATION_HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    """Saves the current translation history to a JSON file."""
    with open(TRANSLATION_HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

# Define our new agent with instructions to be a translator.
translator_agent: Agent = Agent(
    name="UrduTranslator",
    instructions="You are an expert translator. Your sole purpose is to translate text from English to Urdu. Provide only the translated text, without any additional explanations.",
    model=model
)

# Start the interactive translation experience.
print("--- Welcome to the English to Urdu Translator ---")
print("Enter an English phrase to get the translation.")
print("Type 'history' to view previous translations.")
print("Type 'quit' or 'exit' to end the session.\n")

# Load existing history at the start of the program.
translation_history = load_history()

while True:
    try:
        # Get user input for the text they want to translate.
        english_text = input("English text: ")
        
        # Exit the loop if the user types 'quit' or 'exit'.
        if english_text.lower() in ["quit", "exit"]:
            print("--- Goodbye! ---")
            break
        
        # Check for the new 'history' command.
        if english_text.lower() == "history":
            print("\n--- Translation History ---")
            if not translation_history:
                print("No history yet.")
            else:
                for item in translation_history:
                    print(f"English: {item['english']}")
                    print(f"Urdu: {item['urdu']}\n")
            continue

        # Check if the user entered an empty line.
        if not english_text.strip():
            continue

        # Run the agent with the English text.
        print("\nTranslating...")
        result = Runner.run_sync(translator_agent, english_text, run_config=config)
        urdu_translation = result.final_output

        # Print the agent's translated response.
        print(f"Urdu Translation: {urdu_translation}\n")
        
        # Add the new translation to the history.
        translation_history.append({"english": english_text, "urdu": urdu_translation})
        # Save the updated history to the file.
        save_history(translation_history)

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        break

