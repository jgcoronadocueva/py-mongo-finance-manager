# src/services/categoryService.py
from app.models.Category import create_category, get_categories


def add_category(user_id, name, category_type):
    """
    Add a new category for a user.
    """
    create_category(user_id, name, category_type)


def list_categories(user_id):
    """
    Get all categories for a user as a list of dictionaries.
    """
    return get_categories(user_id)
