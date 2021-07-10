"""API layer for the book_management service."""
# pylint: disable=no-member, unexpected-keyword-arg
from typing import Optional, Union
from uuid import uuid4

from chalice import Blueprint

from restless_services.book_management import business
from restless_services.book_management.api_schemas import (
    CreateBookBodySchema,
    CreateBookGenreBodySchema,
    DeleteBookGenresQuerySchema,
    UpdateBookBodySchema,
    UpdateBookGenreBodySchema
)
from utils.api_handler import api_handler

api = Blueprint(__name__)


@api_handler(
    api=api,
    path='/book-management',
    methods=['POST'],
    body_schema=CreateBookBodySchema,
)
def create_user_book() -> Optional[dict]:
    """Creates a new book associated with the user using the given body parameters.

    Returns:
        A dict containing aggregated information for the newly created book else None.
    """
    return business.create_user_book(
        user_id=api.handled_request.user_id,
        author=api.handled_request.body.get('author'),
        title=api.handled_request.body.get('title'),
        primary_genre_id=api.handled_request.body.get('primary_genre_id'),
        image_key=api.handled_request.body.get('image_key'),
        synopsis=api.handled_request.body.get('synopsis'),
        secondary_genre_names=api.handled_request.body.get('secondary_genre_names'),
        book_id=api.handled_request.body.get('book_id')
    )


@api_handler(
    api=api,
    path='/book-management/genres',
    methods=['POST'],
    body_schema=CreateBookGenreBodySchema
)
def create_secondary_book_genre() -> Optional[dict]:
    """Creates a new secondary genre tied to the given book ID.

    Returns:
        A book populated with the updated aggregated information else None.
    """
    return business.create_secondary_book_genre(
        user_id=api.handled_request.user_id,
        book_id=api.handled_request.body.get('book_id'),
        secondary_genre_name=api.handled_request.body.get('secondary_genre_name')
    )


@api_handler(api=api, path='/book-management', methods=['GET'])
def get_user_books() -> list:
    """Gets all of the books associated with the user_id authorized using the given JWT.

    Returns:
        A list of all books associated with the given user_id else an empty list.
    """
    return business.get_user_books(
        user_id=api.handled_request.user_id
    )


@api_handler(api=api, path='/book-management/{book_id}', methods=['GET'])
def get_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a user book by a given ID.

    Args:
        book_id: The unique ID associated with the book being retrieved.

    Returns:
        A book populated with aggregated information else None.
    """
    return business.get_user_book_by_id(
        user_id=api.handled_request.user_id,
        book_id=book_id
    )


@api_handler(
    api=api,
    path='/book-management/{book_id}',
    methods=['PATCH'],
    body_schema=UpdateBookBodySchema
)
def update_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Updates a book with the given ID using the parameters passed in the body of the request.

    Args:
        book_id: The unique ID of the book that needs to be updated.

    Returns:
        A book populated with the updated aggregated information else None.
    """
    return business.update_user_book_by_id(
        user_id=api.handled_request.user_id,
        book_id=book_id,
        title=api.handled_request.body.get('title'),
        author=api.handled_request.body.get('author'),
        synopsis=api.handled_request.body.get('synopsis'),
        image_key=api.handled_request.body.get('image_key'),
        book_status_id=api.handled_request.body.get('book_status_id')
    )


@api_handler(
    api=api,
    path='/book-management/genres/{book_genre_id}',
    methods=['PATCH'],
    body_schema=UpdateBookGenreBodySchema
)
def update_user_book_genre_by_id(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Updates a book genre with the given ID using the params passed in the body of the request.

    Args:
        book_genre_id: The unique ID of the book genre to update.

    Returns:
        An updated book genre else None.
    """
    return business.update_user_book_genre_by_id(
        user_id=api.handled_request.user_id,
        book_id=api.handled_request.body.get('book_id'),
        genre_name=api.handled_request.body.get('genre_name'),
        book_genre_id=book_genre_id
    )


@api_handler(api=api, path='/book-management', methods=['DELETE'])
def delete_user_books() -> list:
    """Deletes all of the books associated with the user_id pulled from the authorized JWT.

    Returns:
        A list of all of the books that were deleted.
    """
    return business.delete_user_books(user_id=api.handled_request.user_id)


@api_handler(api=api, path='/book-management/{book_id}', methods=['DELETE'])
def delete_user_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes the book by the given ID.

    Args:
        book_id: The unique ID of the book to be deleted.

    Returns:
        The deleted book else None.
    """
    return business.delete_user_book_by_id(
        user_id=api.handled_request.user_id,
        book_id=book_id
    )


@api_handler(
    api=api,
    path='/book-management/genres/{book_genre_id}',
    methods=['DELETE'],
    query_schema=DeleteBookGenresQuerySchema
)
def delete_secondary_book_genre(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes the secondary genre from the given book.

    Args:
        book_id: The unique ID of the book to disassociate the secondary genre from.

    Returns:
        The deleted genre else None.
    """
    return business.delete_secondary_book_genre(
        user_id=api.handled_request.user_id,
        book_id=api.handled_request.query.get('book_id'),
        book_genre_id=book_genre_id
    )
