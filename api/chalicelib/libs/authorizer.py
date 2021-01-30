"""Authorizer for Chalice."""
from settings.app import AUTHORIZER_ARN


class JwtOrApiKeyAuthorizer:
    """Authorizer class that accepts a JWT or API key."""
    name = 'jwt-or-api-key'
    _AUTH_TYPE = 'custom'

    def __init__(self, authorizer_uri: str, invoke_role_arn: str = None) -> None:
        self._authorizer_uri = authorizer_uri
        self._invoke_role_arn = invoke_role_arn


authorizer = JwtOrApiKeyAuthorizer(authorizer_uri=AUTHORIZER_ARN)
