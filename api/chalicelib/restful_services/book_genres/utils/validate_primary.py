"""Helper function to validate the primary genre of a book."""
# pylint: disable=no-else-raise
from typing import Union
from uuid import uuid4

from exceptions.restful_service import ModifyingPrimaryException, MultiplePrimaryException
from restful_services.book_genres import data
from restful_services.books import business as books_service
from restful_services.genres import business as genres_service


def validate_primary_genre(
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4],
    method: str = 'POST'
) -> None:
    """Validates that a transation won't lead to a violation in the primary genre requirement.

    Args:
        book_id: The unique ID of the book involved in the transation.
    """
    genre = genres_service.get_genre_by_id(genre_id)
    if genre.get('is_primary'):
        if method == 'POST' and (primary_book_genre := data.get_primary_genre_by_book_id(book_id)):
            raise MultiplePrimaryException(
                book=books_service.get_book_by_id(book_id),
                new_primary=genre.get('name'),
                existing_primary=primary_book_genre.get('genre', {}).get('name')
            )
        elif method == 'PATCH':
            raise ModifyingPrimaryException(book=books_service.get_book_by_id(book_id))
