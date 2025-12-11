"""
Personal Finance Tracker
This program allows a user to track their income and expenses.
It provides a simple menu-driven interface to add transactions,
view the transaction history, and check the current balance.
All data is stored persistently in a text file named 'transactions.txt'.
"""

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Finance Tracker Menu ---")
    print("1. Add a new transaction")
    print("2. View all transactions")
    print("3. Check current balance")
    print("4. Exit")

def get_valid_amount():
    """
    Prompts the user for an amount until a valid number is entered.
    Returns the valid amount as a float.
    """
    while True:
        try:
            return float(input("Enter the amount: $"))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def add_transaction():
    """Adds a new transaction (income or expense) to the file."""
    # Get transaction type
    while True:
        trans_type = input("Is this an 'income' or 'expense'? ").lower()
        if trans_type in ['income', 'expense']:
            break
        print("Please enter either 'income' or 'expense'.")
    
    # Get a valid amount using the helper function
    amount = get_valid_amount()
    
    # Get description
    description = input("Enter a description: ")
    
    # Append the new transaction to the file
    with open("transactions.txt", "a") as file:
        file.write(f"{trans_type},{amount},{description}\n")
    
    print("Transaction added successfully!")

def load_transactions():
    """
    Loads all transactions from the 'transactions.txt' file.
    Returns a list of dictionaries, where each dictionary represents a transaction.
    If the file doesn't exist, it returns an empty list.
    """
    transactions = []
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                # Remove newline and split the line
                parts = line.strip().split(',')
                # Create a dictionary for the transaction
                transaction = {
                    'type': parts[0],
                    'amount': float(parts[1]),
                    'description': parts[2]
                }
                transactions.append(transaction)
    except FileNotFoundError:
        print("No previous transactions found.")
    return transactions

def view_transactions():
    """Displays all stored transactions in a readable format."""
    transactions = load_transactions()
    if transactions:
        print("\n--- Transaction History ---")
        for trans in transactions:
            # Format the amount to always show 2 decimal places
            formatted_amount = f"${trans['amount']:.2f}"
            print(f"{trans['type'].capitalize()}: {formatted_amount} - {trans['description']}")
    else:
        print("No transactions to display.")

def check_balance():
    """Calculates and displays the current account balance."""
    transactions = load_transactions()
    total_income = 0.0
    total_expense = 0.0

    for trans in transactions:
        if trans['type'] == 'income':
            total_income += trans['amount']
        elif trans['type'] == 'expense':
            total_expense += trans['amount']

    balance = total_income - total_expense
    print(f"\nCurrent Balance: ${balance:.2f}")

def main():
    """The main entry point of the program. Runs the menu loop."""
    print("Welcome to the Personal Finance Tracker!")
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Thank you for using the Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

# This ensures the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()