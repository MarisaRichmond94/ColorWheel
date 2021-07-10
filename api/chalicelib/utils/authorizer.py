"""Custom authorizer used for authenticated endpoints."""
from chalice import AuthResponse

from restful_services.sessions.business import get_session_by_token
from restless_services.authentication.business import authenticate_user
from utils.app import APP
from utils import db


@APP.authorizer()
def authorizer(auth_request) -> AuthResponse:
    """Authorizes the bearer token sent up in an authenticated request.

    Args:
        auth_request - The request sent to the chalice application.

    Returns:
        An auth response containing allowed routes and a principal id.
    """
    if auth_request.token:
        with db.session_scope() as db_session:
            db.SESSION = db_session
            json_web_token = auth_request.token.split('Bearer')[1].strip()
            session = get_session_by_token(token=json_web_token)

            if session:
                decoded_payload = authenticate_user(
                    email=session.get('user', {}).get('email'),
                    password=session.get('user', {}).get('password'),
                    json_web_token=json_web_token,
                )

                if decoded_payload:
                    return AuthResponse(
                        context={'user_id': session.get('user', {}).get('id')},
                        routes=['*'],
                        principal_id=decoded_payload.get('sub'),
                    )

    return AuthResponse(routes=[], principal_id='user')
