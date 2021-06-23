"""API layer for the book_management service."""
# pylint: disable=no-member
from typing import Optional, Union
from uuid import uuid4

from chalice import Blueprint

from restless_services.book_management import business
from restless_services.book_management.api_schemas import PostBookManagementBodySchema
from utils.api_handler import api_handler

api = Blueprint(__name__)


@api_handler(
    api=api,
    path='/book-management',
    methods=['POST'],
    body_schema=PostBookManagementBodySchema,
)
def create_book() -> Optional[dict]:
    pass # TODO


@api_handler(api=api, path='/book-management', methods=['GET'])
def get_user_books() -> list:
    pass # TODO


@api_handler(api=api, path='/book-management/{book_id}', methods=['GET'])
def get_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO


@api_handler(api=api, path='/book-management/{book_id}', methods=['PATCH'])
def update_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO


@api_handler(api=api, path='/book-management', methods=['DELETE'])
def delete_user_books() -> list:
    pass # TODO


@api_handler(api=api, path='/book-management/{book_id}', methods=['DELETE'])
def delete_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    pass # TODO
