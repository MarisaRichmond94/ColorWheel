"""Business layer for the sessions service."""
from typing import Optional

from utils.types import UUIDType
from utils.validation import validate_params
from restful_services.sessions.data_layer import data


def create_session(
    user_id: UUIDType,
    token: str,
) -> Optional[dict]:
    """Creates a new session in the fct_sessions table.

    Args:
        user_id - The primary key associated with a user entity in the dim_users table.
        token - An encoded JSON web token associated with the given user entity.

    Returns:
        A newly created session else None.

    Raises:
        InvalidParamException - If the user_id or token is None.
    """
    validate_params(
        func="create_session",
        params={"user_id": user_id, "token": token},
    )
    return data.create_session(user_id=user_id, token=token)


def get_session_by_token(token: str) -> Optional[dict]:
    """Gets a session using the given token.

    Args:
        token - An encoded JSON web token associated with a session in the fct_sessions table.

    Returns:
        A session with the given token else None.

    Raises:
        InvalidParamException - If the token is None.
    """
    validate_params(
        func="get_session_by_token",
        params={"token": token},
    )
    return data.get_session_by_token(token=token)


def get_session_by_user(user_id: UUIDType) -> Optional[dict]:
    """Gets a session using the given user_id.

    Args:
        user_id - The primary key associated with a user entity in the dim_users table.

    Returns:
        A session with the given user_id else None.

    Raises:
        InvalidParamException - If the user_id is None.
    """
    validate_params(
        func="get_session_by_user",
        params={"user_id": user_id},
    )
    return data.get_session_by_user(user_id=user_id)
