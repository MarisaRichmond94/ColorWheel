"""Main application for Chalice APIs"""
# pylint: disable=wrong-import-position
import os
import sys

import alembic.config
from chalice import Chalice

sys.path.insert(0, os.path.abspath("chalicelib"))
from libs.response import Response
from restful_services.users.api_layer.api import api as users_api


app = Chalice(app_name="colorwheel")
app.register_blueprint(users_api)


@app.route("/users", methods=["OPTIONS"])
@app.route("/users/{user_id}", methods=["OPTIONS"])
def set_cors_access_control(*args, **kwargs) -> Response:
    """Sets the CORS access for the OPTIONS endpoint

    Args:
        *args: Arguments passed in to the endpoint
        **kwargs: Keyword arguments passed in to the endpoint

    Returns:
        Response object
    """
    log.info("OPTIONS...")
    headers = {
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*",
    }
    origin = app.current_request.headers.get("origin", "")
    log.debug(f"OPTIONS headers: {headers}, origin: {origin}")
    return Response(data=None, headers=headers, origin=origin)

@app.route('/health')
def check_health():
    """Endpoint for checking the health of the chalice services

    Returns:
        Response containing message 'Service is healthy!'
    """
    return Response(
        message='Service is healthy!', origin=app.current_request.headers.get('origin', '')
    )


@app.lambda_function()
def migrate_db(event, context) -> None:
    """Lambda function to run the alembic migration

    Args:
        event: AWS lambda event object
        context: AWS lambda context object
    """
    alembic_args = [
        "--raiseerr",
        "--config",
        "chalicelib/alembic.ini",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembic_args)
