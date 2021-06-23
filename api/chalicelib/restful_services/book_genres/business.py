"""Business layer for the book_genres service."""
from typing import Optional, Union
from uuid import uuid4

from restful_services.book_genres import data
from restful_services.book_genres.utils.validate_primary import validate_primary_genre
from utils.validation import validate_entity_is_unique, validate_params


def create_book_genre(
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4],
    book_genre_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new book_genre.

    Args:
        book_id: The FK to the books table.
        genre_id: The FK to the genres table.
        book_genre_id: The PK to assign to the new book_genre.

    Returns:
        A newly created book_genre else None.

    Raises:
        InvalidParamException: If any of the given params are None.
        UniqueEntityException: If a book_id/genre_id match already exists in the table.
        MultiplePrimaryException: If the given book id already has a primary genre.
    """
    validate_params(
        func='create_book_genre',
        params={'book_id': book_id, 'genre_id': genre_id}
    )
    validate_entity_is_unique(
        func=data.get_book_genres_by_book_id_and_genre_id,
        book_id=book_id,
        genre_id=genre_id
    )
    validate_primary_genre(book_id=book_id, genre_id=genre_id, method='POST')

    return data.create_book_genre(
        book_id=book_id,
        genre_id=genre_id,
        book_genre_id=book_genre_id
    )


def get_book_genres(book_id: Optional[Union[str, uuid4]]) -> list:
    """Gets book_genres from the table filtered by given params.

    Args:
        book_id: The FK to the book table.

    Returns:
        A list of book_genres filtered by any given params.
    """
    if book_id:
        return data.get_book_genres_by_book_id(book_id)
    return []


def get_book_genre_by_id(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a book_genre from the table by a given id.

    Args:
        book_genre_id: The PK of a book_genre.

    Returns:
        A book_genre from the table by a given id else None.

    Raises:
        InvalidParamException: If the given book_genre_id is None.
    """
    validate_params(
        func='get_book_genre_by_id',
        params={'book_genre_id': book_genre_id}
    )
    return data.get_book_genre_by_id(book_genre_id)


def update_book_genre(
    genre_id: Union[str, uuid4],
    book_genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Updates a book_genre by a given id.

    Args:
        genre_id: The FK to the genre table.
        book_genre_id: The PK of a book_genre.

    Returns:
        An updated book_genre with the given id else None.

    Raises:
        InvalidParamException: If any of the given params are None.
        UniqueEntityException: If a book_id/genre_id match already exists in the table.
        ModifyingPrimaryException: If attempting to modify to replace the book's primary genre.
    """
    validate_params(
        func='update_book_genre',
        params={'genre_id': genre_id, 'book_genre_id': book_genre_id}
    )
    validate_entity_is_unique(
        func=data.get_book_genres_by_book_id_and_genre_id,
        book_id=data.get_book_genre_by_id(book_genre_id).get('book', {}).get('id'),
        genre_id=genre_id
    )
    validate_primary_genre(
        book_id=data.get_book_genre_by_id(book_genre_id).get('book', {}).get('id'),
        genre_id=genre_id,
        method='PATCH'
    )

    return data.update_book_genre(
        genre_id=genre_id,
        book_genre_id=book_genre_id
    )


def delete_book_genres(
    book_id: Union[str, uuid4],
) -> Optional[list]:
    """Deletes book_genres from the table using the given params.

    Args:
        book_id: The FK to the book table.

    Returns:
        A list of book_genres deleted using the given params.

    Raises:
        InvalidParamException: If any of the given params are None.
    """
    validate_params(func='delete_book_genres', params={'book_id': book_id})
    return data.delete_book_genres(book_id)


def delete_book_genre_by_id(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a book_genre from the table by the given id.

    Args:
        book_genre_id: The PK of a book_genre.

    Returns:
        A deleted book_genre with the given id else None.

    Raises:
        InvalidParamException: If the given book_genre_id is None.
    """
    validate_params(func='delete_book_genre_by_id', params={'book_genre_id': book_genre_id})
    return data.delete_book_genre_by_id(book_genre_id)
