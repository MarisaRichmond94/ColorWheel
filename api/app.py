"""Main application for Chalice APIs"""
# pylint: disable=wrong-import-position
import os
import sys

from chalice import Chalice

sys.path.insert(0, os.path.abspath("chalicelib"))
from libs.response import Response
# from restless_services.authentication.api_layer.api import api as authentication_api


app = Chalice(app_name='colorwheel')

# @app.register_blueprint(authentication_api)


# @app.route('/authentication', methods=['OPTIONS'])

@app.route('/health')
def check_health():
    """Endpoint for checking the health of the chalice services

    Returns:
        Response containing message 'Service is healthy!'
    """
    return Response(
        message='Service is healthy!', origin=app.current_request.headers.get('origin', '')
    )
