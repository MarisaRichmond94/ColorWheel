from chalice import AuthResponse

from utils.app import APP


@APP.authorizer()
def authorizer(auth_request) -> AuthResponse:
    is_authenticated = authenticate_user(
        user_email=auth_request.headers.get('email'),
        json_web_token=auth_request.token,
    )
    return (
        AuthResponse(routes=['/'], principal_id='user')
        if is_authenticated else AuthResponse(routes=[], principal_id='user')
    )
