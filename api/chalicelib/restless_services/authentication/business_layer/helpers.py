from io import BytesIO
from typing import Dict

import jwt


def encode_json_web_token(user: Dict) -> str:
    payload = {
        "iss": "colorwheel",
        "exp": 1200,
        "sub": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email")
    }
    return jwt.encode(payload, user.get("password"), algorithm="HS256")


def decode_json_web_token(json_web_token: str, secret: str) -> Dict:
    return jwt.decode(json_web_token, secret, algorithms=["HS256"])
