"""Data layer for the users service."""
from typing import Optional

from db_models.dim_users import DimUsers
from utils import db
from restful_services.users.model_layer.data_schemas import UserSchema


def create_user(
    name: str,
    email: str,
    password: bytes,
) -> Optional[dict]:
    """Creates a new user in the dim_users table.

    Args:
        name: The full name (first and last) of a user.
        email: The unique email address to associated with the new user.
        password: A plain text string containing at least 10 characters.

    Returns:
        A newly created user else None.
    """
    with db.session_scope() as session:
        user = DimUsers(
            name=name,
            email=email,
            password=password,
        )

        if user:
            session.add(user)
            session.commit()
            return UserSchema().dump(user)

        return None


def get_user_by_email(email: str) -> Optional[dict]:
    """Gets a user by the given email.

    Args:
        email: The unique email address associated with a user entity in the dim_users table.

    Returns:
        A user associated with the given email else None.
    """
    with db.session_scope() as session:
        user = session.query(DimUsers).filter_by(email=email).one_or_none()
        return UserSchema().dump(user) if user else None
