# pylint: disable=wrong-import-position
import os
import sys

import alembic.config
from chalice import Chalice

sys.path.insert(0, os.path.abspath("chalicelib"))
from utils.app import create_chalice_app

app = create_chalice_app()

from utils.response import Response
from restless_services.authentication.api_layer.api import api as authentication_api


app.register_blueprint(authentication_api)

@app.route("/authentication", methods=["OPTIONS"])
def set_cors_headers(*args, **kwargs) -> Response:
    return Response(
        data=None,
        headers={
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Expose-Headers": "*",
        },
        origin=app.current_request.headers.get("origin", "")
    )

@app.route('/health')
def check_health() -> Response:
    return Response(message='healthy', origin=app.current_request.headers.get('origin', ''))


@app.lambda_function()
def migrate_db(event, context) -> None:
    alembic.config.main(argv=[ "--config", "chalicelib/alembic.ini", "upgrade", "head" ])
