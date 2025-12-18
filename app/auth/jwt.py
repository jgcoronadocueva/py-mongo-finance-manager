# app/auth/jwt.py
import jwt
from datetime import datetime, timedelta, timezone
from app.config.settings import JWT_SECRET


def create_token(user_id):
    """
    Create a JWT token for a user with a set expiration.
    """
    # Contains the payload with the data to transmit
    payload = {
        "user_id": str(user_id),
        "iat": datetime.now(timezone.utc),  # Issued at
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),  # Expiration time
    }

    # Encode the payload with JWT secret key
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def verify_token(token):
    """
    Verify a JWT token and return the payload if valid.
    """
    try:
        # Decode the token with the secret key
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token")
        return None
