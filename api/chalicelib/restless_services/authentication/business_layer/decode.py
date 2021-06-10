"""Decode helper function for the authentication service."""
import jwt


def decode_json_web_token(json_web_token: str, secret: str) -> dict:
    """Decodes a json_web_token using the given secret.

    Args:
        json_web_token - An encoded JSON web token.
        secret - A hashed and salted string.

    Returns:
        A decoded payload.
    """
    return jwt.decode(
        json_web_token,
        secret,
        algorithms=['HS256'],
        options={'require': ['exp', 'iss', 'sub', 'name', 'email']},
    )
