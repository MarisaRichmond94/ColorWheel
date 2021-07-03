"""Restless service level exceptions."""


class UnauthorizedAccessException(Exception):
    """An exception that indicates an attempt to access data not tied to the user accessing."""
    def __init__(self, accessing_user_id, data, authorized_user_id):
        """Generates message using given variables."""
        self.message = (
            f'Users with id "{accessing_user_id}" attempted to access the following data belonging '
            f'to user with id "{authorized_user_id}": {data}.'
        )
        super().__init__(self.message)
