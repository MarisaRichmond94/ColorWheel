"""Wrapper functionality for handling API requests/responses."""
import functools

from chalice import Blueprint
from loguru import logger as log
import marshmallow

from utils.authorizer import authorizer
from utils.request import validate_request
from utils.response import generate_fail_response, generate_success_response, Response


def api_handler(
    api: Blueprint,
    path: str,
    methods: list,
    *,
    api_key_required: bool = True,
    body_schema: marshmallow.Schema = None,
    query_schema: marshmallow.Schema = None
) -> Response:
    """Generates API response using given variables."""
    def wrapped_api(func):
        @api.route(
            path=path,
            methods=methods,
            api_key_required=api_key_required,
            authorizer=authorizer if api_key_required else None
        )
        @functools.wraps(func)
        def api_endpoint(*args, **kwargs):
            log.debug(f'{func.__name__} received {methods[0]} request.')
            request, error_response = validate_request(
                current_request=api.current_request,
                body_schema=body_schema,
                query_schema=query_schema,
            )

            if error_response:
                return error_response

            api.handled_request = request
            api.handled_request.user_id = (
                api.current_request.context.get('authorizer', {}).get('user_id')
            )

            try:
                data = func(*args, **kwargs)
            except Exception as api_handler_exception:
                log.exception(api_handler_exception)
                return generate_fail_response(path, api.current_request.headers.get('origin', ''))

            if data is None:
                log.error(f'{func.__name__} {methods[0]} request resulted in None response.')
                return generate_fail_response(path, api.current_request.headers.get('origin', ''))

            log.debug(f'{func.__name__} {methods[0]} request result: {data}.')
            return generate_success_response(api.current_request, data, api_key_required)

        return api_endpoint

    return wrapped_api
