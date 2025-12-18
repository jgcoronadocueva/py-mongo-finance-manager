# app/menu.py
from app.auth.authService import register, login
from app.auth.jwt import verify_token
from app.services.transactionService import (
    create_transaction,
    show_transactions,
    edit_transaction,
    remove_transaction
)


def run_menu():
    current_token = None

    while True:
        print("\n=== Personal Finance Manager ===")
        print("1. Register")
        print("2. Login")
        print("3. Add transaction")
        print("4. View transactions")
        print("5. Update transaction")
        print("6. Delete transaction")
        print("7. Logout")
        print("8. Exit")

        choice = input("Choose: ")

        # REGISTER
        if choice == "1":
            register(
                input("Username: "),
                input("Password: "),
                input("First name: "),
                input("Last name: "),
                input("Email: ")
            )

        # LOGIN
        elif choice == "2":
            result = login(
                input("Username: "),
                input("Password: ")
            )

            if result:
                current_token, _ = result
                print("Logged in")

        # ADD TRANSACTION (CREATE)
        elif choice == "3":
            if not current_token:
                print("Please login first")
                continue

            payload = verify_token(current_token)
            if not payload:
                current_token = None
                continue

            create_transaction(
                payload["user_id"],
                float(input("Amount: ")),
                input("Category: ")
            )

        # VIEW TRANSACTIONS (READ)
        elif choice == "4":
            if not current_token:
                print("Please login first")
                continue

            payload = verify_token(current_token)
            if not payload:
                current_token = None
                continue

            show_transactions(payload["user_id"])

        # UPDATE TRANSACTION
        elif choice == "5":
            if not current_token:
                print("Please login first")
                continue

            edit_transaction(
                input("Transaction ID: "),
                float(input("New amount: "))
            )

        # DELETE TRANSACTION
        elif choice == "6":
            if not current_token:
                print("Please login first")
                continue

            remove_transaction(input("Transaction ID: "))

        # LOGOUT
        elif choice == "7":
            current_token = None
            print("Logged out")

        # EXIT
        elif choice == "8":
            print("Goodbye")
            break

        else:
            print("Invalid option")