"""Data layer for the sessions service."""
from typing import Optional, Union
from uuid import uuid4

from db_models.fct_sessions import FctSessions
from restful_services.sessions.data_schemas import (
    PopulatedSessionSchema,
    SessionSchema,
)
from utils import db


def create_session(user_id: Union[str, uuid4], token: str) -> Optional[dict]:
    """Creates a new session in the fct_sessions table.

    Args:
        user_id: The primary key associated with a user entity in the dim_users table.
        token: An encoded JSON web token associated with the given user entity.

    Returns:
        A newly created session else None.
    """
    new_session = FctSessions(
        id=uuid4(),
        dim_user_id=user_id,
        token=token
    )

    if new_session:
        db.SESSION.add(new_session)
        return SessionSchema().dump(new_session)

    return None


def get_session_by_token(token: str) -> Optional[dict]:
    """Gets a session using the given token.

    Args:
        token: An encoded JSON web token associated with a session in the fct_sessions table.

    Returns:
        A session with the given token else None.
    """
    retrieved_session = db.SESSION.query(FctSessions).filter_by(token=token).one_or_none()
    return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None


def get_session_by_user(user_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a session using the given user_id.

    Args:
        user_id: The primary key associated with a user entity in the dim_users table.

    Returns:
        A session with the given user_id else None.
    """
    retrieved_session = db.SESSION.query(FctSessions).filter_by(dim_user_id=user_id).one_or_none()
    return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None
