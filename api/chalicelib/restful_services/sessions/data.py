"""Data layer for the sessions service."""
from typing import Optional

from db_models.fct_sessions import FctSessions
from utils import db
from utils.types import UUIDType
from restful_services.sessions.data_schemas import (
    PopulatedSessionSchema,
    SessionSchema,
)


def create_session(user_id: UUIDType, token: str) -> Optional[dict]:
    """Creates a new session in the fct_sessions table.

    Args:
        user_id - The primary key associated with a user entity in the dim_users table.
        token - An encoded JSON web token associated with the given user entity.

    Returns:
        A newly created session else None.
    """
    with db.session_scope() as session:
        new_session = FctSessions(
            dim_user_id=user_id,
            token=token
        )

        if new_session:
            session.add(new_session)
            session.commit()
            return SessionSchema().dump(new_session)

        return None


def get_session_by_token(token: str) -> Optional[dict]:
    """Gets a session using the given token.

    Args:
        token - An encoded JSON web token associated with a session in the fct_sessions table.

    Returns:
        A session with the given token else None.
    """
    with db.session_scope() as session:
        retrieved_session = session.query(FctSessions).filter_by(token=token).one_or_none()
        return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None


def get_session_by_user(user_id: UUIDType) -> Optional[dict]:
    """Gets a session using the given user_id.

    Args:
        user_id - The primary key associated with a user entity in the dim_users table.

    Returns:
        A session with the given user_id else None.
    """
    with db.session_scope() as session:
        retrieved_session = session.query(FctSessions).filter_by(dim_user_id=user_id).one_or_none()
        return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None
