"""Main application for Chalice APIs"""
# pylint: disable=wrong-import-position
import os
import sys

import alembic.config
from chalice import Chalice, AuthResponse

sys.path.insert(0, os.path.abspath("chalicelib"))
from utils.app import create_chalice_app
from utils.response import Response
from restless_services.authentication.api_layer.api import api as authentication_api
from restless_services.authentication.business_layer.business import authenticate_user


app = create_chalice_app()
# app.register_blueprint(users_api)

@app.authorizer()
def authorizer(auth_request) -> AuthResponse:
    """Authorizes the JSON web token on an auth_request.

    Args:
        auth_request - The request to chalice

    Returns:
        AuthResponse object containing authorized routes and principal_id
    """
    is_authenticated = authenticate_user(json_web_token=auth_request.token)
    return (
        AuthResponse(routes=['/'], principal_id='user')
        if is_authenticated else AuthResponse(routes=[], principal_id='user')
    )



@app.route("/authentication", methods=["OPTIONS"])
def set_cors_access_control(*args, **kwargs) -> Response:
    """Sets the CORS access for the OPTIONS endpoint

    Args:
        *args: Arguments passed in to the endpoint
        **kwargs: Keyword arguments passed in to the endpoint

    Returns:
        Response object
    """
    return Response(
        data=None,
        headers={
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        },
        origin=app.current_request.headers.get("origin", "")
    )

@app.route('/health')
def check_health():
    """Endpoint for checking the health of the chalice services

    Returns:
        Response containing message 'Service is healthy!'
    """
    return Response(message='healthy', origin=app.current_request.headers.get('origin', ''))


@app.lambda_function()
def migrate_db(event, context) -> None:
    """Lambda function to run the alembic migration

    Args:
        event: AWS lambda event object
        context: AWS lambda context object
    """
    alembic_args = [ "--raiseerr", "--config", "chalicelib/alembic.ini", "upgrade", "head" ]
    alembic.config.main(argv=alembic_args)
