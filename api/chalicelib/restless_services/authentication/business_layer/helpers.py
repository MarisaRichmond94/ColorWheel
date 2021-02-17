import datetime
from math import floor

import jwt


def encode_json_web_token(user: dict) -> tuple:
    payload = {
        "iss": "colorwheel",
        "exp": floor((datetime.datetime.utcnow() + datetime.timedelta(minutes=20)).timestamp()),
        "sub": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
    }
    return jwt.encode(payload, user.get("password"), algorithm="HS256"), payload


def decode_json_web_token(json_web_token: str, secret: str) -> dict:
    return jwt.decode(
        json_web_token,
        secret,
        algorithms=["HS256"],
        options={"require": ["exp", "iss", "sub", "name", "email"]},
    )
