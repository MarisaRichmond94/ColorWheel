"""Helper functions for the authentication service"""
import BytesIO
from typing import Dict

import jwt


def encode_json_web_token(user: Dict, private_key: str) -> str:
    """Encodes a new JSON web token (jwt) using the given information

    Args:
        user: A dict containing information about a user
        private_key: A base64 encoded string

    Returns:
        A JSON web token
    """
    private_key = convert_to_bytesIO(decoded_string=private_key)
    payload = {
        "iss": "colorwheel",
        "exp": 1200,
        "sub": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email")
    }

    return jwt.encode(payload, private_key, algorithm="RS256")


def decode_json_web_token(json_web_token: str, public_key: str) -> Dict:
    """Decodes a given JSON web token (jwt)

    Returns:
        A dict containing the information stored in the json_web_token
    """
    public_key = convert_to_bytesIO(decoded_string=public_key)
    return jwt.decode(json_web_token, public_key, algorithms=["RS256"])


def convert_to_bytesIO(decoded_string: str) -> BytesIO:
    """Encodes a new JSON web token (jwt) using the given information

    Args:
        decoded_string: A base64 decoded string

    Returns:
        A BytesIO string
    """
    return BytesIO(base64.b64decode(decoded_string)).read()
