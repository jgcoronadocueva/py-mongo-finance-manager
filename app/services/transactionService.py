# src/services/transactionService.py
from app.models.Transaction import (
    create_transaction,
    get_transactions,
    update_transaction,
    delete_transaction,
)


def add_transaction(user_id, amount, category):
    """
    Add a new transaction for a user.
    """
    return create_transaction(user_id, amount, category)


def show_transactions(user_id):
    """
    Get all transactions for a user.
    """
    return get_transactions(user_id)


def edit_transaction(transaction_id, amount=None, category=None):
    """
    Edit a transaction's amount and/or category.
    """
    updates = {}

    # Add fields to updates if they are provided
    if amount is not None:
        updates["amount"] = amount
    if category is not None:
        updates["category"] = category

    # If there is no update
    if not updates:
        return False

    # Update the transaction data in the database
    return update_transaction(transaction_id, updates)


def remove_transaction(transaction_id):
    """
    Delete a transaction.
    """
    return delete_transaction(transaction_id)
