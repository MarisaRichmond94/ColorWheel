"""Business layer for the authentication service."""
from typing import Optional

from loguru import logger as log

from restful_services.sessions.business_layer.business import create_session
from restful_services.users.business_layer.business import (
    create_user,
    get_user_by_email
)
from restful_services.users.business_layer.helpers import validate_password
from restless_services.authentication.business_layer.helpers import (
    decode_json_web_token,
    encode_json_web_token
)
from utils.validation import validate_params


def authorize_user(
    email: str,
    password: str,
    name: Optional[str] = None,
) -> Optional[dict]:
    """Authorizes a user with the users service using the given params.

    Args:
        email - The unique email associated with a user entity in the dim_users table.
        password - The plain string password associated with a user entity in the dim_users table.
        name - The full name of a new user.

    Returns:
        A dict containing an access token and auth results else None.

    Raises:
        InvalidParamException - If email or password is None.
    """
    validate_params(
        func="authorize_user",
        params={"email": email, "password": password}
    )

    user = (
        create_user(name=name, email=email, password=password)
        if name else get_user_by_email(email=email)
    )
    if not user:
        log.debug(
            f'Failed to GET user by email "{email}" from Users Service.'
            if not name else f'Failed to POST new user with name "{name}" and email "{email}".'
        )
        return None

    is_user_validated = (
        validate_password(password=password, hashed=user.get('password'))
        if not name else True
    )
    if not is_user_validated:
        log.debug(
            f'Failed to validate given plain text password "{password}" with the entity '
            f'associated with the given email "{email}".'
        )
        return None

    access_token, auth_results = encode_json_web_token(user=user)
    create_session(user_id=user.get('id'), token=access_token)

    return {
        'access_token': access_token,
        'auth_results': auth_results
    }


def refresh_authorization(email: str) -> Optional[dict]:
    """Refreshes the authenication token for a user session with the given email.

    Args:
        email - The unique email associated with a session entity in the fct_sessions table.

    Returns:
        A dict containing an access token and auth results else None.

    Raises:
        InvalidParamException - If the given email is None.
    """
    validate_params(
        func="refresh_authorization",
        params={"email": email},
    )

    user = get_user_by_email(email=email)
    if not user:
        log.debug(f'Failed to GET user by email "{email}" from Users Service.')
        return None

    access_token, auth_results = encode_json_web_token(user=user)
    create_session(user_id=user.get('id'), token=access_token)

    return {
        'access_token': access_token,
        'auth_results': auth_results
    }


def authenticate_user(
    email: str,
    password: str,
    json_web_token: str,
) -> Optional[dict]:
    """Authenticates a user's json web token with the given parameters.

    Args:
        email - The unique email associated with a user entity in the dim_users table.
        password - The plain string password associated with a user entity in the dim_users table.

    Returns:
        A dict containing the decoded json web token.

    Raises:
        InvalidParamException - If any of the given params is None.
    """
    validate_params(
        func="authenticate_user",
        params={
            "email": email,
            "password": password,
            "json_web_token": json_web_token,
        }
    )

    user = get_user_by_email(email=email)
    if not user:
        log.debug(f'Failed to GET user by email "{email}" from Users Service.')
        return None
    if not password == user.get('password'):
        log.debug(
            f'Failed to validate given plain text password "{password}" with the entity '
            f'associated with the given email "{email}".'
        )
        return None

    return decode_json_web_token(
        json_web_token=json_web_token,
        secret=user.get('password'),
    )
