"""Chalice request helpers"""
import marshmallow

from libs.response import Response


class Request:
    """Custom Request object"""
    headers = {}
    query = {}
    body = {}
    form = {}

    def __str__(self) -> str:
        return f"Request(headers={self.headers}, query='{self.query}', body={self.body})"


def validate_request(
    current_request: object = None,
    body_schema: marshmallow.Schema = None,
    query_schema: marshmallow.Schema = None,
) -> (object, dict):
    """Parses and validates a request against a marshmallow Schema

    Args:
        current_request: The current request object
        body_schema: The marshmallow schema representing the valid request body arguments
        query_schema: The marshmallow schema representing the valid request query arguments

    Returns:
        A tuple of the new request object with only the valid parameters and an error response if
            the parsing encountered issues
    """
    request = Request()
    error_data = {}

    if query_schema:
        try:
            request.query = query_schema().load(current_request.query_params or {})
        except marshmallow.exceptions.ValidationError as exc_info:
            error_data['query'] = exc_info.messages

    if body_schema:
        try:
            json_body = current_request.json_body or {}
            if isinstance(json_body, list):
                request.body = body_schema(many=True).load(json_body or {})
            else:
                request.body = body_schema().load(json_body or {})
        except marshmallow.exceptions.ValidationError as exc_info:
            error_data['body'] = exc_info.messages

    if error_data:
        response = Response(
            status_code=400,
            message='Invalid request.',
            data=error_data
        )
        return request, response

    return request, None
