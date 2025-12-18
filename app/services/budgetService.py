# src/services/budgetService.py
from app.models.Budget import set_budget, get_budgets

def create_budget(user_id, category, limit_amount):
    set_budget(user_id, category, limit_amount)

def show_budgets(user_id):
    for b in get_budgets(user_id):
        print(f"{b['category']} → ${b['limit']}")