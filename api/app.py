import os
import sys

sys.path.insert(0, os.path.abspath('chalicelib'))
from utils.app import create_chalice_app

app = create_chalice_app()

from utils.response import Response
from restless_services.authentication.api import api as authentication_api
from restless_services.book_management.api import api as book_management_api


app.register_blueprint(authentication_api)
app.register_blueprint(book_management_api)

@app.route('/authentication', methods=['OPTIONS'])
@app.route('/book-management', methods=['OPTIONS'])
@app.route('/book-management/{book_id}', methods=['OPTIONS'])
@app.route('/book-management/genres', methods=['OPTIONS'])
@app.route('/book-management/genres/{book_genre_id}', methods=['OPTIONS'])
def set_cors_headers() -> Response:
    return Response(
        data=None,
        headers={
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Expose-Headers': '*',
        },
        origin=app.current_request.headers.get('origin', '')
    )

@app.route('/health')
def check_health() -> Response:
    return Response(message='healthy', origin=app.current_request.headers.get('origin', ''))
