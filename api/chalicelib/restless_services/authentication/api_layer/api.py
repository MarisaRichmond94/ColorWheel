from chalice import Blueprint
from loguru import logger as log

from utils.request import validate_request
from utils.response import Response
from restless_services.authentication.business_layer import business
from restless_services.authentication.model_layer.api_schemas import (
    GetAuthenticationQuerySchema,
    PostAuthenticationBodySchema,
)

api = Blueprint(__name__)


@api.route(
    "/authentication",
    methods=["POST"]
)
def authorize_user() -> Response:
    log.debug("Authentication Service recieved a POST request to create a new user.")
    request, error_response = validate_request(
        current_request=api.current_request,
        body_schema=PostAuthenticationBodySchema,
    )

    if error_response:
        return error_response

    try:
        auth_results = business.authorize_user(
            email=request.body.get("email"),
            password=request.body.get("password"),
            name=request.body.get("name"),
        )
    except Exception as authorize_user_exception:
        log.exception(authorize_user_exception)
        return Response(
            status_code=500,
            message="Error occurred for POST in Authentication API",
            origin=api.current_request.headers.get("origin", ""),
        )

    if not auth_results:
        log.error("POST to Authentication Service failed to authorize user.")
        return Response(
            status_code=403,
            message="Unauthorized User",
            origin=api.current_request.headers.get("origin", ""),
        )

    return Response(
        data=auth_results,
        origin=api.current_request.headers.get("origin", ""),
    )


@api.route(
    "/authentication",
    methods=["GET"]
)
def refresh_authorization() -> Response:
    log.debug("Authentication Service recieved a POST request to create a new user.")
    request, error_response = validate_request(
        current_request=api.current_request,
        query_schema=GetAuthenticationQuerySchema,
    )

    if error_response:
        return error_response

    try:
        auth_results = business.refresh_authorization(email=request.query.get("email"))
    except Exception as refresh_authorization_exception:
        log.exception(refresh_authorization_exception)
        return Response(
            status_code=500,
            message="Error occurred for GET in Authentication API",
            origin=api.current_request.headers.get("origin", ""),
        )

    if not auth_results:
        log.error("GET to Authentication Service failed to get refreshed JSON web token.")
        return Response(
            status_code=403,
            message="Unauthorized User",
            origin=api.current_request.headers.get("origin", ""),
        )

    return Response(
        data=auth_results,
        origin=api.current_request.headers.get("origin", ""),
    )
