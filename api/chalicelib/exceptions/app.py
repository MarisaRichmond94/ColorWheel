"""Custom app exceptions"""


class InvalidParamException(Exception):
    """Class for invalid parameter exception"""

    def __init__(self, func, keys):
        """Sets message using invalid parameters"""
        self.message = f'Function "{func}" missing required parameter(s): {str(keys)}.'
        super().__init__(self.message)
