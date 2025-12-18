# app/services/userService.py
from app.models.User import get_user_by_username, update_user


def update_username(user_id, new_username):
    """
    Update a user's username.
    """
    # Check if the new username already exists
    if get_user_by_username(new_username):
        return False

    # Update the username in the database
    return update_user(user_id, {"username": new_username})


def update_profile(user_id, first_name=None, last_name=None, email=None):
    """
    Update user's profile information.
    Only updates fields that are provided.
    """
    updates = {}

    # Add fields to updates if they are provided
    if first_name is not None:
        updates["firstName"] = first_name
    if last_name is not None:
        updates["lastName"] = last_name
    if email is not None:
        updates["email"] = email

    # If there is no update
    if not updates:
        return False

    # Update the user profile info in the database
    return update_user(user_id, updates)
