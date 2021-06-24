"""Restful service level exceptions."""


class ModifyingPrimaryException(Exception):
    """An exception that indicates an attempt to modify an existing primary genre for a book."""
    def __init__(self, book):
        """Generates message using given variables."""
        self.message = (
            f'Attempting to modify the primary genre for book with name "{book.get("title")}".'
        )
        super().__init__(self.message)


class MultiplePrimaryException(Exception):
    """An exception that indicates an attempt to add two primary genres to a book."""
    def __init__(self, book, new_primary, existing_primary):
        """Generates message using given variables."""
        self.message = (
            f'Attempting to attach primary book genre "{new_primary}" to book with name '
            f'"{book.get("title")}" that already has an existing primary genre: '
            f'"{existing_primary}"'
        )
        super().__init__(self.message)


class UniqueEntityException(Exception):
    """An exception that indicates that a uniqueness check has failed."""
    def __init__(self, func, value, **kwargs):
        """Generates message using given variables."""
        self.message = (
            f'Function "{func}" given arguments "{kwargs}" returned the following '
            f'matching entity: {value}.'
        )
        super().__init__(self.message)
