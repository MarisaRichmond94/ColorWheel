"""Data layer for the users service."""
from typing import Optional
from uuid import uuid4

from db_models.dim_users import DimUsers
from restful_services.users.data_schemas import UserSchema


def create_user(
    session: any,
    name: str,
    email: str,
    password: bytes,
) -> Optional[dict]:
    """Creates a new user in the dim_users table.

    Args:
        session: The current database session.
        name: The full name (first and last) of a user.
        email: The unique email address to associated with the new user.
        password: A plain text string containing at least 10 characters.

    Returns:
        A newly created user else None.
    """
    user = DimUsers(
        id=uuid4(),
        name=name,
        email=email,
        password=password
    )

    if user:
        session.add(user)
        return UserSchema().dump(user)
    return None


def get_user_by_email(session: any, email: str) -> Optional[dict]:
    """Gets a user by the given email.

    Args:
        session: The current database session.
        email: The unique email address associated with a user entity in the dim_users table.

    Returns:
        A user associated with the given email else None.
    """
    user = session.query(DimUsers).filter_by(email=email).one_or_none()
    return UserSchema().dump(user) if user else None
