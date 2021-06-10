"""Application level exceptions."""


class InvalidParamException(Exception):
    """An exception that indicates that a None-type value was given to a function."""
    def __init__(self, func, keys):
        """Generates message using given variables."""
        self.message = f'Function '{func}' missing required parameter(s): {str(keys)}.'
        super().__init__(self.message)
