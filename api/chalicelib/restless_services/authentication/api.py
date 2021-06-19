"""API layer for the authentication service."""
# pylint: disable=no-member
from typing import Optional

from chalice import Blueprint

from restless_services.authentication import business
from restless_services.authentication.api_schemas import (
    GetAuthenticationQuerySchema,
    PostAuthenticationBodySchema,
)
from utils.api_handler import api_handler

api = Blueprint(__name__)


@api_handler(
    api=api,
    path='/authentication',
    methods=['POST'],
    api_key_required=False,
    body_schema=PostAuthenticationBodySchema,
)
def authorize_user() -> Optional[dict]:
    """Authorizes a user with the users service using the given params.

    Returns:
        A dict containing an access token and auth results else None.
    """
    return business.authorize_user(
        email=api.handled_request.body.get('email'),
        password=api.handled_request.body.get('password'),
        name=api.handled_request.body.get('name'),
    )


@api_handler(
    api=api,
    path='/authentication',
    methods=['GET'],
    api_key_required=False,
    query_schema=GetAuthenticationQuerySchema,
)
def refresh_authorization() -> Optional[dict]:
    """Refreshes the authenication token for a user session with the given email.

    Returns:
        A dict containing an access token and auth results else None.
    """
    return business.refresh_authorization(
        email=api.handled_request.query.get('email'),
    )
