"""Business layer for the book_statuses service."""
from restful_services.book_statuses.data_layer import data


def get_book_statuses() -> list:
    """Gets book statuses from the dim_book_statuses table.

    Returns:
        A list of book statuses.
    """
    return data.get_book_statuses()
