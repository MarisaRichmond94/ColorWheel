"""Chalice request helpers"""
import cgi
from io import BytesIO

import marshmallow
from loguru import logger as log

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
    headers_schema: marshmallow.Schema = None,
    form_schema: marshmallow.Schema = None,
) -> (object, dict):
    """Parses and validates a request against a marshmallow Schema

    Args:
        current_request: The current request object
        body_schema: The marshmallow schema representing the valid request body arguments
        query_schema: The marshmallow schema representing the valid request query arguments
        headers_schema: The marshmallow schema representing the valid request header arguments
        form_schema: The marshmallow schema representing the valid form data arguments

    Returns:
        A tuple of the new request object with only the valid parameters and an error response if
          the parsing encountered issues
    """
    request = Request()
    error_data = {}
    if headers_schema:
        try:
            request.headers = headers_schema().load(current_request.headers or {})
        except marshmallow.exceptions.ValidationError as exc_info:
            error_data['headers'] = exc_info.messages

    if query_schema:
        try:
            request.query = query_schema().load(current_request.query_params or {})
        except marshmallow.exceptions.ValidationError as exc_info:
            error_data['query'] = exc_info.messages

    if form_schema:
        try:
            multipart_form_data = get_flattened_multipart_form_data(current_request)
            request.form = form_schema().load(multipart_form_data)
        except marshmallow.exceptions.ValidationError as exc_info:
            error_data['body'] = exc_info.messages

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
            status_code=400, message='Invalid request.', data=error_data)
        log.info(request)
        log.info(response)
        return request, response

    return request, None


def get_flattened_multipart_form_data(current_request: object) -> dict:
    """Parses the multipart/form-data content type from a request

    Args:
        current_request: The request to parse

    Returns:
        A dictionary of form keys to form values
    """
    raw_body = BytesIO(current_request.raw_body)
    content_type = current_request.headers.get('content-type')
    _, parameters = cgi.parse_header(content_type)
    parameters['boundary'] = parameters.get('boundary').encode('utf-8')
    parsed = cgi.parse_multipart(raw_body, parameters)

    return {key: value[0] for key, value in parsed.items()}
