# src/services/transactionService.py
from app.models.Transaction import (
    add_transaction,
    get_transactions,
    update_transaction,
    delete_transaction
)

def create_transaction(user_id, amount, category):
    add_transaction(user_id, amount, category)
    print("Transaction inserted")

def show_transactions(user_id):
    for t in get_transactions(user_id):
        print(f"{t['_id']} | {t['category']} → ${t['amount']}")

def edit_transaction(transaction_id, amount=None, category=None):
    if update_transaction(transaction_id, amount, category):
        print("Transaction modified")
    else:
        print("Nothing updated")

def remove_transaction(transaction_id):
    if delete_transaction(transaction_id):
        print("Transaction deleted")
    else:
        print("Transaction not found")