"""Business layer for the users service."""
from typing import Optional

from utils.validation import validate_params
from restful_services.users import data
from restful_services.users.utils import hash_password


def create_user(
    name: str,
    email: str,
    password: str,
) -> Optional[dict]:
    """Creates a new user in the dim_users table.

    Args:
        name: The full name (first and last) of a user.
        email: The unique email address to associated with the new user.
        password: A plain text string containing at least 10 characters.

    Returns:
        A newly created user else None.

    Raises:
        InvalidParamException - if any of the given params are None.
    """
    validate_params(
        func='create_user',
        params={
            'name': name,
            'email': email,
            'password': password
        },
    )
    hashed_password = hash_password.generate_hashed_password(password=password)
    return data.create_user(
        name=name,
        email=email,
        password=hashed_password,
    )


def get_user_by_email(email: str) -> Optional[dict]:
    """Gets a user by the given email.

    Args:
        email: The unique email address associated with a user entity in the dim_users table.

    Returns:
        A user associated with the given email else None.

    Raises:
        InvalidParamException - if email is None.
    """
    validate_params(
        func='get_user_by_email',
        params={'email': email},
    )
    return data.get_user_by_email(email=email)
