"""Data layer for the book_statuses service."""
from db_models.dim_book_statuses import DimBookStatuses
from restful_services.book_statuses.data_schemas import BookStatusesSchema
from utils import db


def get_book_statuses() -> list:
    """Gets all book statuses from the dim_book_statuses table.

    Returns:
        A list of book statuses.
    """
    with db.session_scope() as session:
        book_statuses = session.query(DimBookStatuses).all()
        return BookStatusesSchema(many=True).dump(book_statuses) if book_statuses else []
