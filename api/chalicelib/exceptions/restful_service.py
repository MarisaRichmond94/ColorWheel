"""Restful level exceptions."""


class UniqueEntityException(Exception):
    """An exception that indicates that a uniqueness check has failed."""
    def __init__(self, func, value, **kwargs):
        """Generates message using given variables."""
        self.message = (
            f'Function "{func}" given arguments "{str(**kwargs)}" returned the following '
            f'matching entity: {value}.'
        )
        super().__init__(self.message)
