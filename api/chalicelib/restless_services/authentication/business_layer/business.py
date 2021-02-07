from typing import Dict, Optional

from loguru import logger as log

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
    name: Optional[str] = None
) -> Dict:
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
        return None

    access_token, auth_results = encode_json_web_token(user=user)

    return {
        'access_token': access_token,
        'auth_results': auth_results
    }


def refresh_authorization(email: str) -> Optional[str]:
    validate_params(func="refresh_authorization", params={ "email": email })

    user = get_user_by_email(email=email)
    if not user:
        log.debug(f'Failed to GET user by email "{email}" from Users Service.')
        return None

    access_token, auth_results = encode_json_web_token(user=user)

    return {
        'access_token': access_token,
        'auth_results': auth_results
    }


def authenticate_user(user_email: str, json_web_token: str) -> bool:
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
