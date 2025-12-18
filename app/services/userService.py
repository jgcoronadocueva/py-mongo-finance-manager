# app/services/userService.py
from app.models.User import get_user_by_username, update_user

def update_username(user_id, new_username):
    if get_user_by_username(new_username):
        print("Username already taken")
        return False

    return update_user(user_id, {"username": new_username})


def update_profile(user_id, first_name=None, last_name=None, email=None):
    updates = {}

    if first_name is not None:
        updates["firstName"] = first_name
    if last_name is not None:
        updates["lastName"] = last_name
    if email is not None:
        updates["email"] = email

    if not updates:
        print("Nothing to update")
        return False

    return update_user(user_id, updates)