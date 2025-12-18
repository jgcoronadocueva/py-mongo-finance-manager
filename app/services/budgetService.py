# src/services/budgetService.py
from app.models.Budget import set_budget, get_budgets


def create_budget(user_id, category, limit_amount):
    """
    Set or update a budget limit for a user.
    """
    return set_budget(user_id, category, limit_amount)


def show_budgets(user_id: str):
    """
    Get all budgets for a user as a list of dictionaries.
    """
    return get_budgets(user_id)
