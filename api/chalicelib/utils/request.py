"""Module for handling Chalice Requests."""
import marshmallow

from utils.response import Response


class Request:
    """Custom request class."""
    headers = {}
    query = {}
    body = {}
    form = {}


def __str__(self) -> str:
    return f'Request(body={self.body}, query="{self.query}", headers={self.headers})'


def validate_request(
    current_request: object = None,
    body_schema: marshmallow.Schema = None,
    query_schema: marshmallow.Schema = None,
) -> tuple:
    """Validates a request using given request and optional schema."""
    request = Request()
    error_info = {}

    if body_schema:
        try:
            json_body = current_request.json_body or {}
            if isinstance(json_body, list):
                request.body = body_schema(many=True).load(json_body or {})
            else:
                request.body = body_schema().load(json_body or {})
        except marshmallow.exceptions.ValidationError as schema_exception:
            error_info['body'] = schema_exception.messages

    if query_schema:
        try:
            request.query = query_schema().load(current_request.query_params or {})
        except marshmallow.exceptions.ValidationError as schema_exception:
            error_info['query'] = schema_exception.messages

    if error_info:
        response = Response(
            status_code=400,
            message='Invalid request.',
            data=error_info
        )
        return request, response

    return request, None
