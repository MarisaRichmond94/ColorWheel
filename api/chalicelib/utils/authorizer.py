from chalice import AuthResponse

from restful_services.sessions.business_layer.business import get_session_by_token
from restless_services.authentication.business_layer.business import authenticate_user
from utils.app import APP


@APP.authorizer()
def authorizer(auth_request) -> AuthResponse:
    if auth_request.token:
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
                    routes=['*'],
                    principal_id=decoded_payload.get('sub'),
                )

    return AuthResponse(routes=[], principal_id='user')
