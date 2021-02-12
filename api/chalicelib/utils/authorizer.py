from chalice import AuthResponse

from restless_services.authentication.business_layer.business import authenticate_user
from utils.app import APP


@APP.authorizer()
def authorizer(auth_request) -> AuthResponse:
    if auth_request.token:
        auth_info = auth_request.token.split('Bearer')[1].strip()
        json_web_token, email = auth_info.split(',')
        decoded_payload = authenticate_user(
            email=email,
            json_web_token=json_web_token,
        )

        if decoded_payload:
            return AuthResponse(
                routes=['*'],
                principal_id=decoded_payload.get('sub'),
            )

    return AuthResponse(routes=[])
