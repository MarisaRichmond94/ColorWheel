"""API layer for the books service."""
from typing import Optional

from chalice import Blueprint

from restful_services.books import business
from restful_services.books.api_schemas import (
    DeleteBooksQuerySchema,
    GetBooksQuerySchema,
    UpdateBookBodySchema,
    CreateBookBodySchema
)
from utils.api_handler import api_handler

api = Blueprint(__name__)
ROUTE = '/books'
ENTITY_ID = '/{book_id}'


@api_handler(
    api,
    path=ROUTE,
    methods=['POST'],
    body_schema=CreateBookBodySchema
)
def create_book() -> Optional[dict]:
    """Creates a new book in the table.

    Returns:
        A newly created book else None.
    """
    return business.create_book(
        user_id=api.handled_request.user_id,
        author=api.handled_request.body.get('author'),
        image_key=api.handled_request.body.get('image_key'),
        summary=api.handled_request.body.get('summary'),
        title=api.handled_request.body.get('title'),
        book_id=api.handled_request.body.get('id')
    )


@api_handler(
    api,
    path=ROUTE,
    methods=['GET'],
    query_schema=GetBooksQuerySchema
)
def get_books() -> list:
    """Gets books from the table filtered by given params.

    Returns:
        A list of books filtered by any given params.
    """
    return business.get_books(user_id=api.handled_request.query.get('user_id'))


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['GET']
)
def get_book_by_id(book_id: str) -> Optional[dict]:
    """Gets a book from the table by a given id.

    Args:
        book_id: The primary key of a book.

    Returns:
        A book from the table by a given id else None.
    """
    return business.get_book_by_id(book_id)


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['PATCH'],
    body_schema=UpdateBookBodySchema
)
def update_book(book_id: str) -> Optional[dict]:
    """Updates a book in the table by a given id.

    Args:
        book_id: The primary key of a book.

    Returns:
        An updated book with the given id else None.
    """
    return business.update_book(
        book_id=book_id,
        user_id=api.handled_request.user_id,
        title=api.handled_request.body.get('title'),
        author=api.handled_request.body.get('author'),
        summary=api.handled_request.body.get('summary'),
        image_key=api.handled_request.body.get('image_key'),
        book_status_id=api.handled_request.body.get('book_status_id')
    )


@api_handler(
    api,
    path=ROUTE,
    methods=['DELETE'],
    query_schema=DeleteBooksQuerySchema
)
def delete_books() -> Optional[list]:
    """Deletes books from the table using the given params.

    Returns:
        A list of books deleted using the given params.
    """
    return business.delete_books(user_id=api.handled_request.query.get('user_id'))


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['DELETE']
)
def delete_book_by_id(book_id: str) -> Optional[dict]:
    """Deletes a book from the table by the given id.

    Args:
        book_id: The primary key of a book.

    Returns:
        A deleted book with the given id else None.
    """
    return business.delete_book_by_id(book_id)
