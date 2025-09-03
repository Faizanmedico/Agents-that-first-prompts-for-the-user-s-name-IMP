# main_loan_eligibility_agent.py
# This file defines and runs a Loan Eligibility Agent that uses a simulated tool.

print("Script started!") # Debug print to confirm execution begins

from agents import Agent, Runner
# CORRECTED IMPORT: Changed 'conection' to 'connection' to match your filename.
from connection import config, model 

# --- Our Simulated Tool: Loan Eligibility Checker ---
# This function acts as our "tool" that the agent will "use".
# It takes simulated financial data and determines eligibility based on simple rules.
def check_loan_eligibility(credit_score: int, annual_income: float, debt_to_income_ratio: float) -> str:
    """
    Simulates checking loan eligibility based on provided financial criteria.
    This is a simplified, hypothetical check for demonstration purposes.
    """
    print(f"\n(Simulating tool call: check_loan_eligibility(credit_score={credit_score}, annual_income={annual_income}, debt_to_income_ratio={debt_to_income_ratio}))\n")

    # Simple eligibility rules (these are just examples)
    if credit_score >= 680 and annual_income >= 50000 and debt_to_income_ratio <= 0.40:
        return "Based on the provided simulated data, you appear to be **Eligible** for a loan."
    elif credit_score >= 600 and annual_income >= 30000 and debt_to_income_ratio <= 0.50:
        return "Based on the provided simulated data, you might be **Conditionally Eligible** for a loan, possibly with different terms."
    else:
        return "Based on the provided simulated data, you appear to be **Not Eligible** for a loan at this time."

# --- The Loan Eligibility Agent ---
loan_agent: Agent = Agent(
    name="Loan Eligibility Specialist",
    instructions="""
    You are a professional and helpful Loan Eligibility Specialist for "First Citizen's Bank".
    Your primary role is to provide general guidance on loan eligibility based on **simulated financial data** provided by the user.

    # Key Instructions:
    - **Simulated Data Only**: Explicitly state that you are an AI and cannot process real personal or financial data. All inputs are hypothetical for educational purposes.
    - **Use the Eligibility Checker**: When the user provides a credit score, annual income, and debt-to-income ratio, you must use the `check_loan_eligibility` tool (which will be provided to you) to determine their simulated eligibility.
    - **Explain Results Clearly**: Present the eligibility result from the tool in a clear, polite, and reassuring manner.
    - **Privacy Reminder**: Reiterate that this is a simulation and for actual loan applications, they must visit the official First Citizen's Bank website or a branch.
    - **Do NOT ask for real personal information.**
    """,
    model=model
)

# --- Interactive Session ---
print("--- Welcome to the First Citizen's Bank Loan Eligibility Assistant ---")
print("I can help you understand general loan eligibility based on **simulated** financial data.")
print("Please provide a **hypothetical credit score (e.g., 720), annual income (e.g., 65000), and debt-to-income ratio (e.g., 0.30)**.")
print("Example input: 720, 65000, 0.30")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    try:
        user_input = input("Enter simulated data (Credit Score, Annual Income, DTI): ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("\nThank you for using our service. Have a great day!")
            break

        if not user_input.strip():
            continue

        # Parse the user's input for the simulated tool call
        try:
            parts = [float(p.strip()) for p in user_input.split(',')]
            if len(parts) != 3:
                print("Invalid input format. Please enter three numbers separated by commas (Credit Score, Annual Income, DTI).")
                continue
            
            simulated_credit_score = int(parts[0])
            simulated_annual_income = parts[1]
            simulated_debt_to_income_ratio = parts[2]

        except ValueError:
            print("Invalid input. Please ensure all values are numbers.")
            continue

        # --- How the "Tool" is Used ---
        # We call our simulated tool function directly here.
        simulated_eligibility_result = check_loan_eligibility(
            simulated_credit_score,
            simulated_annual_income,
            simulated_debt_to_income_ratio
        )

        # We then craft the prompt for the agent, including the result from our "tool".
        # This is how the agent "knows" the tool's output without directly calling it from the model.
        prompt_for_agent = (
            f"The user provided the following simulated financial data: "
            f"Credit Score: {simulated_credit_score}, Annual Income: ${simulated_annual_income:,.2f}, "
            f"Debt-to-Income Ratio: {simulated_debt_to_income_ratio:.2f}. "
            f"Based on this, the simulated eligibility check result is: '{simulated_eligibility_result}'. "
            f"Please respond to the user based on this information, following your instructions."
        )
        
        print("Consulting the Loan Eligibility Specialist...")
        
        result = Runner.run_sync(loan_agent, prompt_for_agent, run_config=config)
        agent_response = result.final_output

        print(f"\n{agent_response}\n")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application or try a different input.")
        break

