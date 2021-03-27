"""Data layer for the book_statuses service."""
from db_models.dim_book_statuses import DimBookStatuses
from utils import db
from restful_services.book_statuses.model_layer.data_schemas import BookStatusesSchema


def get_book_statuses() -> list:
    """Gets all book statuses from the dim_book_statuses table.

    Returns:
        A list of book statuses.
    """
    with db.session_scope() as session:
        book_statuses = session.query(DimBookStatuses).all()
        return BookStatusesSchema(many=True).dump(book_statuses) if book_statuses else []
