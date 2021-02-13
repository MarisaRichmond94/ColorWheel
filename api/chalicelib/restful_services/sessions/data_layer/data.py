from typing import Optional

from db_models.fct_sessions import FctSessions
from utils import db
from utils.types import UUIDType
from restful_services.sessions.model_layer.data_schemas import (
    PopulatedSessionSchema,
    SessionSchema,
)


def create_session(user_id: UUIDType, token: str) -> Optional[dict]:
    with db.session_scope() as session:
        new_session = FctSessions(dim_user_id=user_id, token=token)

        if new_session:
            session.add(new_session)
            session.commit()
            return SessionSchema().dump(new_session)

        return None


def update_session(user_id: UUIDType, token: str) -> Optional[dict]:
    with db.session_scope() as session:
        updated_session = session.query(FctSessions).filter_by(dim_user_id=user_id).one_or_none()

        if updated_session:
            updated_session.token = token
            session.commit()
            return PopulatedSessionSchema().dump(updated_session)

        return None


def get_session_by_token(token: str) -> Optional[dict]:
    with db.session_scope() as session:
        retrieved_session = session.query(FctSessions).filter_by(token=token).one_or_none()
        return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None


def get_session_by_user(user_id: UUIDType) -> Optional[dict]:
    with db.session_scope() as session:
        retrieved_session = session.query(FctSessions).filter_by(dim_user_id=user_id).one_or_none()
        return PopulatedSessionSchema().dump(retrieved_session) if retrieved_session else None
