"""Business layer for the authentication service"""
from typing import Optional

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
) -> tuple[Optional[str], Optional[Dict]]:
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
        func="authorize_user"
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

    private_public_key = get_private_public_key()
    if not private_public_key:
        log.debug('Failed to GET private_public_key from PrivatePublicKeys Service.')
        return None, None

    private_key = download_s3_object(
        bucket_name=AUTHENTICATION_BUCKET_NAME,
        object_key=private_public_key.get("private_pem_object_key"),
    )
    if not private_key:
        log.debug('Failed to GET private key from S3.')
        return None, None

    json_web_token = encode_json_web_token(
        user=user,
        private_key=private_key,
    )

    return json_web_token, user


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
    log.debug(f'Failed to GET user by email "{email}" from Users Service.')
    if not user:
        return None

    private_public_key = get_private_public_key()
    if not private_public_key:
        log.debug('Failed to GET private_public_key from PrivatePublicKeys Service.')
        return None

    private_key = download_s3_object(
        bucket_name=AUTHENTICATION_BUCKET_NAME,
        object_key=private_public_key.get("private_pem_object_key"),
    )
    if not private_key:
        log.debug('Failed to GET private key from S3.')
        return None

    return encode_json_web_token(user=user, private_key=private_key)


def authenticate_user(json_web_token: str) -> bool:
    """Authenticates a user's JSON web token

    Args:
        json_web_token: A signed JSON web token

    Returns:
        True or False
    """
    private_public_key = get_private_public_key()
    if not private_public_key:
        log.debug('Failed to GET private_public_key from PrivatePublicKeys Service.')
        return False

    public_key = download_s3_object(
        bucket_name=AUTHENTICATION_BUCKET_NAME,
        object_key=private_public_key.get("public_pem_object_key"),
    )
    if not public_key:
        log.debug('Failed to GET public key from S3.')
        return False

    decoded_payload = decode_json_web_token(json_web_token=json_web_token, public_key=public_key)
    return True if decoded_payload else False
