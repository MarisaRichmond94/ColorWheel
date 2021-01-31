"""Custom app exceptions"""


class InvalidParamException(Exception):
    """Class for invalid parameter exception"""

    def __init__(self, keys):
        """Sets message using invalid parameters"""
        self.message = f"Missing required parameter(s): {str(keys)}."
        super().__init__(self.message)
