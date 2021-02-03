"""Helper functions for the authentication service"""
from io import BytesIO
from typing import Dict

import jwt


def encode_json_web_token(user: Dict) -> str:
    """Encodes a new JSON web token (jwt) using the given information

    Args:
        user: A dict containing information about a user

    Returns:
        A JSON web token
    """
    payload = {
        "iss": "colorwheel",
        "exp": 1200,
        "sub": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email")
    }

    return jwt.encode(payload, user.get('password'), algorithm="RS256")


def decode_json_web_token(json_web_token: str, secret: str) -> Dict:
    """Decodes a given JSON web token (jwt)

    Args:
        json_web_token: The json_web_token belonging to the user
        secret: The user's hashed password

    Returns:
        A dict containing the information stored in the json_web_token
    """
    return jwt.decode(json_web_token, secret, algorithms=["RS256"])
