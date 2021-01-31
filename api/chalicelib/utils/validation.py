"""Lib for validation functionality"""
from exceptions.app import InvalidParamException


def validate_params(func: str, params: dict) -> None:
    """Validates that all passed params are not None

    Args:
        params: A dict of required arguments and their values

    Raises:
        InvalidParamException: If missing required parameters are missing
        TypeError: If params is not a dictionary
        ValueError: If params is None
    """
    if not func:
        raise ValueError('Missing required parameter "func".')
    if not params:
        raise ValueError('Missing required parameter "params".')

    if not isinstance(params, dict):
        raise TypeError(
            f"Params expected a dictionary but recieved {type(params)}.")

    missing_params = [key for key, value in params.items() if value is None]
    if missing_params:
        raise InvalidParamException(func=func, keys=missing_params)
