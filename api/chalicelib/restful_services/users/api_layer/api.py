"""API layer for the users service"""
from chalice import Blueprint
from loguru import logger as log

from libs.request import validate_request
from libs.response import Response
from restful_services.users.business_layer import business
from restful_services.users.model_layer.api_schemas import (
    CreateUserBodySchema,
)

api = Blueprint(__name__)


@api.route(
    '/users',
    methods=["POST"]
)
def create_user() -> Response:
    """Creates new user in the dim_users table.

    Returns:
        Response object containing the newly created user if successful or a fail message and status
    """
    log.debug("User service received POST request to create a new user.")
    request, error_response = validate_request(
        current_request=api.current_request,
        body_schema=CreateUserBodySchema,
    )

    if error_response:
        return error_response

    try:
        user = business.create_user(
            name=request.body.get("name"),
            email=request.body.get("email"),
            password=request.body.get("password"),
        )
    except Exception as create_user_exception:
        log.exception(create_user_exception)
        return Response(
            status_code=500,
            message="Error occurred for POST in Users API",
            origin=api.current_request.headers.get("origin", ""),
        )

    if not user:
        log.error("POST to Users Service failed to create new user.")
        return Response(
            status_code=500,
            message="Error occurred for POST in Users API",
            origin=api.current_request.headers.get("origin", ""),
        )

    log.debug(f"POST to User Service created new user ${user}")
    return Response(
        data=user,
        origin=api.current_request.headers.get("origin", ""),
    )
