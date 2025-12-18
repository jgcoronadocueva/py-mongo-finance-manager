# app/menu.py
from app.auth.authService import register, login
from app.auth.jwt import verify_token
from app.services.transactionService import (
    add_transaction,
    show_transactions,
    edit_transaction,
    remove_transaction
)

def run_menu():
    current_token = None

    def require_login():
        """
        Check if user is logged in and token is valid
        """
        nonlocal current_token
        if not current_token:
            print("Please login first")
            return None
        payload = verify_token(current_token)
        if not payload:
            print("Session expired or invalid. Please login again.")
            current_token = None
        return payload

    while True:
        print("\n----- Personal Finance Manager -----")
        print("1. Register")
        print("2. Login")
        print("3. Add Transaction")
        print("4. View Transactions")
        print("5. Update Transaction")
        print("6. Delete Transaction")
        print("7. Logout")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1":  # Register
            register(
                input("Username: "),
                input("Password: "),
                input("First Name: "),
                input("Last Name: "),
                input("Email: ")
            )

        elif choice == "2":  # Login
            result = login(input("Username: "), input("Password: "))
            if result:
                current_token, _ = result
                print("Logged in")
            else:
                print("Login failed")

        elif choice == "3":  # Add Transaction
            payload = require_login()
            if payload:
                amount = float(input("Amount: "))
                category = input("Category: ")
                add_transaction(payload["user_id"], amount, category)
                print("Transaction added")

        elif choice == "4":  # View Transactions
            payload = require_login()
            if payload:
                transactions = show_transactions(payload["user_id"])
                if transactions:
                    for t in transactions:
                        print(f"{t['_id']} | {t['category']} → ${t['amount']}")
                else:
                    print("No transactions found.")

        elif choice == "5":  # Update Transaction
            payload = require_login()
            if payload:
                transaction_id = input("Transaction ID: ")
                amount_input = input("New Amount (leave empty to skip): ")
                category_input = input("New Category (leave empty to skip): ")
                amount = float(amount_input) if amount_input else None
                category = category_input if category_input else None
                if edit_transaction(transaction_id, amount, category):
                    print("Transaction updated")
                else:
                    print("Nothing updated")

        elif choice == "6":  # Delete Transaction
            payload = require_login()
            if payload:
                transaction_id = input("Transaction ID: ")
                if remove_transaction(transaction_id):
                    print("Transaction deleted")
                else:
                    print("Transaction not found")

        elif choice == "7":  # Logout
            current_token = None
            print("Logged out")

        elif choice == "8":  # Quit
            print("Goodbye!")
            break

        else:
            print("Invalid option")
