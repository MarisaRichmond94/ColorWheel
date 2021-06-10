"""Module containing validation functionality."""
from exceptions.app import InvalidParamException


def validate_params(func: str, params: dict) -> None:
    """Validates given params are not None.

    Args:
        func - The name of the function params are being validated for.
        params - A dict containing params that are expected to be defined.

    Raises:
        ValueError - if either of the given args are not defined.
        TypeError - if params is not a dictionary.
        InvalidParamException - If any of the given params are None.
    """
    if not func:
        raise ValueError('Missing required parameter 'func'.')
    if not params:
        raise ValueError('Missing required parameter 'params'.')

    if not isinstance(params, dict):
        raise TypeError(
            f'Params expected a dictionary but recieved {type(params)}.')

    missing_params = [key for key, value in params.items() if value is None]
    if missing_params:
        raise InvalidParamException(func=func, keys=missing_params)
