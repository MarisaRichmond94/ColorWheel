from typing import Optional

from utils.types import UUIDType
from utils.validation import validate_params
from restful_services.sessions.data_layer import data


def create_session(user_id: UUIDType, token: str) -> Optional[dict]:
    validate_params(
        func="create_session",
        params={"user_id": user_id, "token": token}
    )

    session = get_session_by_user(user_id=user_id)
    if session:
        return update_session(user_id=user_id, token=token)

    return data.create_session(user_id=user_id, token=token)


def update_session(user_id: UUIDType, token: str) -> Optional[dict]:
    validate_params(
        func="update_session",
        params={"user_id": user_id, "token": token}
    )

    return data.update_session(user_id=user_id, token=token)


def get_session_by_token(token: str) -> Optional[dict]:
    validate_params(func="get_session_by_token", params={"token": token})
    return data.get_session_by_token(token=token)


def get_session_by_user(user_id: UUIDType) -> Optional[dict]:
    return data.get_session_by_user(user_id=user_id)
