"""Encode helper function for the authentication service."""
import datetime
from math import floor

import jwt


def encode_json_web_token(user: dict) -> tuple:
    """Encodes a json_web_token using the given user's information.

    Args:
        user - A user entity from the dim_users table.

    Returns:
        A JSON web token encoded using a salted and hashed password.
    """
    payload = {
        'iss': 'colorwheel',
        'exp': floor((datetime.datetime.utcnow() + datetime.timedelta(minutes=20)).timestamp()),
        'sub': user.get('id'),
        'name': user.get('name'),
        'email': user.get('email'),
    }
    return jwt.encode(payload, user.get('password'), algorithm='HS256'), payload
