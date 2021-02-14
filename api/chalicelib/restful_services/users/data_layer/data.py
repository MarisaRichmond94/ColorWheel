from typing import Optional

from db_models.dim_users import DimUsers
from utils import db
from restful_services.users.model_layer.data_schemas import UserSchema


def create_user(name: str, email: str, password: bytes) -> Optional[dict]:
    with db.session_scope() as session:
        user = DimUsers(
            name=name,
            email=email,
            password=password
        )

        if user:
            session.add(user)
            session.commit()
            return UserSchema().dump(user)

        return None


def get_user_by_email(email: str) -> Optional[dict]:
    with db.session_scope() as session:
        user = session.query(DimUsers).filter_by(email=email).one_or_none()
        return UserSchema().dump(user) if user else None
