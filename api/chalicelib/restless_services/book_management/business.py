"""Business layer for the book_management service."""
from typing import Optional, Union
from uuid import uuid4

from loguru import logger as log

from restful_services.users.utils import validate
from utils.validation import validate_params


def create_book() -> Optional[dict]:
    pass # TODO


def get_user_books() -> list:
    pass # TODO


def get_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO


def update_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO


def delete_user_books() -> list:
    pass # TODO


def delete_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO
