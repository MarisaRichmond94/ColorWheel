"""Business layer for the authentication service"""
from typing import Dict, Optional

from loguru import logger as log

from restful_services.private_public_keys.business_layer.business import get_private_public_key
from restful_services.users.business_layer.business import (
    create_user,
    get_user_by_email
)
from restful_services.users.business_layer.helpers import validate_password
from restless_services.authentication.business_layer.helpers import (
    decode_json_web_token,
    encode_json_web_token
)
from settings.aws import AUTHENTICATION_BUCKET_NAME
from utils.s3 import download_s3_object
from utils.validation import validate_params


def authorize_user(
    email: str,
    password: str,
    name: Optional[str] = None
) -> tuple:
    """Authenticates a new user by creating the new user in the Users Service and generating a
        signed jwt

    Args:
        name: The full name of the new user
        email: The email to associate with the user
        password: The secret string used to validate the user's identity

    Returns:
        A JSON web token and user or None if the user is not authenticated with the users service

    Raises:
        InvalidParamException - when any of the given params are None
    """
    validate_params(
        func="authorize_user",
        params={ "email": email, "password": password }
    )

    user = (
        create_user(name=name, email=email, password=password)
        if name else get_user_by_email(email=email)
    )
    if not user:
        log.debug(
            'Failed to create new user: NoneType returned from Users Service.'
            if name else f'Failed to GET user by email "{email}" from Users Service.'
        )
        return None, None

    return encode_json_web_token(user=user), user


def refresh_authorization(email: str) -> Optional[str]:
    """Reauthenticates a user by generating a new signed jwt

    Args:
        email: The email to associate with the user

    Returns:
        A JSON web token

    Raises:
        InvalidParamException - when email is None
    """
    validate_params(func="refresh_authorization", params={ "email": email })

    user = get_user_by_email(email=email)
    if not user:
        log.debug(f'Failed to GET user by email "{email}" from Users Service.')
        return None

    return encode_json_web_token(user=user)


def authenticate_user(user_email: str, json_web_token: str) -> bool:
    """Authenticates a user's JSON web token

    Args:
        user_email: The email address of the user making the request
        json_web_token: A signed JSON web token

    Returns:
        True or False
    """
    validate_params(
        func="authenticate_user",
        params={ "email": email, "json_web_token": json_web_token }
    )

    user = get_user_by_email(email=email)
    if not user:
        log.debug(f'Failed to GET user by email "{email}" from Users Service.')
        return None

    decoded_payload = decode_json_web_token(
        json_web_token=json_web_token,
        secret=user.get('password'),
    )

    return True if decoded_payload else False
