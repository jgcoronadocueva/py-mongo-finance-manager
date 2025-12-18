# src/services/categoryService.py
from app.models.Category import create_category, get_categories

def add_category(user_id, name, category_type):
    create_category(user_id, name, category_type)

def list_categories(user_id):
    for c in get_categories(user_id):
        print(f"{c['name']} ({c['type']})")