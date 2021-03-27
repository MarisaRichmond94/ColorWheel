"""API layer for the book_statuses service."""
from chalice import Blueprint

from restful_services.book_statuses.business_layer import business
from utils.api_handler import api_handler

api = Blueprint(__name__)


@api_handler(
    api=api,
    path="/book-statuses",
    methods=["GET"],
)
def get_book_statuses() -> list:
    """Gets book statuses from the dim_book_statuses table.

    Returns:
        A list of book statuses.
    """
    return business.get_book_statuses()
