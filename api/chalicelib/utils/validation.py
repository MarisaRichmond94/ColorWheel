from exceptions.app import InvalidParamException


def validate_params(func: str, params: dict) -> None:
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
