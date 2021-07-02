"""Data layer for the book_statuses service."""
from db_models.dim_book_statuses import DimBookStatuses
from restful_services.book_statuses.data_schemas import BookStatusSchema


def get_book_statuses(session: any) -> list:
    """Gets all book statuses from the dim_book_statuses table.

    Args:
        session: The current database session.

    Returns:
        A list of book statuses.
    """
    book_statuses = session.query(DimBookStatuses).all()
    return BookStatusSchema(many=True).dump(book_statuses) if book_statuses else []
