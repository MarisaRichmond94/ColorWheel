"""Authorizer functionality to ensure a user is authenticated with the app"""
from libs.app import APP


@APP.authorizer()
def authorizer(auth_request) -> AuthResponse:
    """Authorizes the JSON web token on an auth_request

    Args:
        auth_request - The request to chalice

    Returns:
        AuthResponse object containing authorized routes and principal_id
    """
    is_authenticated = authenticate_user(
        user_email=auth_request.headers.get('email'),
        json_web_token=auth_request.token,
    )
    return (
        AuthResponse(routes=['/'], principal_id='user')
        if is_authenticated else AuthResponse(routes=[], principal_id='user')
    )
