"""Business layer for the book_statuses service."""
from restful_services.book_statuses import data


def get_book_statuses(session: any) -> list:
    """Gets book statuses from the dim_book_statuses table.

    Args:
        session: The current database session.

    Returns:
        A list of book statuses.
    """
    return data.get_book_statuses(session)
