"""Business layer for the users service"""
from typing import Dict, Optional
from uuid import uuid4

import bcrypt
from loguru import logger as log

from libs.validation import validate_params
from restful_services.users.data_layer import data
from restful_services.users.business_layer.helpers import (
    generate_hashed_password,
    validate_password
)


def create_user(name: str, email: str, password: str) -> Optional[Dict]:
    """Creates new user in the dim_users table

    Args:
        name: The first and last name of the new user
        email: The email to associate with the new user
        password: The secret string need to generate a hash/salt combo to validate a user's identity

    Returns:
        JSON representation of a newly created user from the dim_users table or None

    Raises:
        InvalidParamException - when any of the given params are None
    """
    validate_params(params={ "name": name, "email": email, "password": password })

    hashed_password = generate_hashed_password(password=password)
    return data.create_user(name=name, email=email, password=hashed_password)


def get_user_by_email(email: str) -> Optional[Dict]:
    """Gets user from the dim_users table by email

    Args:
        email: The email to associate with the new user

    Returns:
        JSON representation of a user from the database with matching email or None

    Raises:
        InvalidParamException - when a email is not provided
    """
    validate_params(params={ "email": email })

    return data.get_user_by_email(email=email)
