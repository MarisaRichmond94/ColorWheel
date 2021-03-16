import os
import sys

sys.path.insert(0, os.path.abspath("chalicelib"))
from utils.app import create_chalice_app

app = create_chalice_app()

from utils.response import Response
from restful_services.book_statuses.api_layer.api import api as book_statuses_api
from restless_services.authentication.api_layer.api import api as authentication_api


app.register_blueprint(authentication_api)
app.register_blueprint(book_statuses_api)

@app.route("/authentication", methods=["OPTIONS"])
@app.route("/book-statuses", methods=["OPTIONS"])
def set_cors_headers() -> Response:
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
