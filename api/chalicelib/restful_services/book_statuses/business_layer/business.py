"""Business layer for the book_statuses service."""
from typing import Optional

from utils.types import UUIDType
from utils.validation import validate_params
from restful_services.book_statuses.data_layer import data


def get_book_statuses(
    # pass in variables
) -> list:
    """Gets book statuses from the dim_book_statuses table.

    Returns:
        A list of book statuses.
    """
    return data.get_book_statuses()

