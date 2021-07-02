"""Business layer for the book_management service."""
# pylint: disable=too-many-arguments
from typing import Optional, Union
from uuid import uuid4

from loguru import logger as log

from restful_services.books import business as books_service
from restful_services.book_genres import business as book_genres_service
from restless_services.book_management.utils.populate import populate_genres_for_user_book
from restless_services.book_management.utils import security
from utils.validation import validate_params


def create_user_book(
    user_id: Union[str, uuid4],
    author: str,
    title: str,
    primary_genre_id: Union[str, uuid4],
    image_key: Optional[str],
    synopsis: Optional[str],
    secondary_genre_ids: Optional[list],
    book_id: Optional[Union[str, uuid4]]
) -> Optional[dict]:
    """Creates a new book associated with the user using the given body parameters.

    Args:
        user_id: The unique ID of the user creating the book.
        author: The name of the person writing the book.
        title: The title of the new book.
        primary_genre_id: The unique ID of the primary genre for the book.
        image_key: The S3 object_key associated with the user's book cover.
        synopsis: A short summary of the book.
        secondary_genre_ids: A list of secondary genres to associate with the new book.
        book_id: Optional unique ID to associate with the new book.

    Returns:
        A dict containing aggregated information for the newly created book else None.

    Raises:
        InvalidParamException: If any of the required parameters are None.
    """
    log.info(f'Creating new book "{title}" for user with id "{user_id}".')
    validate_params(
        func='create_user_book',
        params={
            'user_id': user_id,
            'author': author,
            'title': title,
            'primary_genre_id': primary_genre_id
        }
    )

    new_book = books_service.create_book(
        user_id=user_id,
        author=author,
        title=title,
        image_key=image_key,
        synopsis=synopsis,
        book_id=book_id
    )

    primary_book_genre = book_genres_service.create_book_genre(
        book_id=new_book.get('id'),
        genre_id=primary_genre_id
    )

    secondary_book_genres = [
        book_genres_service.create_book_genre(
            book_id=new_book.get('id'),
            genre_id=secondary_genre_id
        )
        for secondary_genre_id in secondary_genre_ids
    ]

    new_book.update({
        'primary_genre': (
            book_genres_service.get_book_genre_by_id(primary_book_genre.get('id'))
        ),
        'secondary_genres': [
            book_genres_service.get_book_genre_by_id(secondary_book_genre.get('id'))
            for secondary_book_genre in secondary_book_genres
        ]
    })

    return new_book


def create_secondary_book_genre(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4],
    secondary_genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Creates a new secondary genre tied to the given book ID.

    Args:
        user_id: The unique ID of the user pulled off of the authorized JWT.
        book_id: The unique ID of the book to tie the new secondary genre to.
        secondary_genre_id: The unique ID of the genre to tie to the book.

    Returns:
        The updated secondary book genre else None.

    Raises:
        InvalidParamException: If any of the required parameters are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(
        f'Tying new secondary genre with id "{secondary_genre_id}" to book with id "{book_id}"'
    )
    validate_params(
        func='create_secondary_book_genre',
        params={'user_id': user_id, 'book_id': book_id, 'secondary_genre_id': secondary_genre_id}
    )
    security.validate_user_book(user_id=user_id, book_id=book_id)

    new_book_genre = book_genres_service.create_book_genre(
        book_id=book_id,
        genre_id=secondary_genre_id
    )
    return book_genres_service.get_book_genre_by_id(new_book_genre.get('id'))


def get_user_books(user_id: Union[str, uuid4]) -> list:
    """Gets all of the books associated with the user ID authorized using the given JWT.

    Args:
        user_id: The unique user ID associated with the JWT authorized in the request.

    Returns:
        A list of all books associated with the given user ID else an empty list.

    Raises:
        InvalidParamException: If the user ID is None.
    """
    log.info(f'Retrieving aggregated book data for user with id "{user_id}".')
    validate_params(func='get_user_books', params={'user_id': user_id})

    return [
        populate_genres_for_user_book(user_book=user_book)
        for user_book in books_service.get_books(user_id=user_id)
    ]

def get_user_book_by_id(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4]
) -> Optional[dict]:
    """Gets a user book by a given ID.

    Args:
        user_id: The unique user ID associated with the JWT authorized in the request.
        book_id: The unique ID associated with the book being retrieved.

    Returns:
        A book populated with aggregated information else None.

    Raises:
        InvalidParamException: If the given user ID or book ID are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(
        f'Attempting to retrieve aggregated book data for book with id "{book_id}" for user with '
        f'id "{user_id}".'
    )
    validate_params(func='get_user_book_by_id', params={'user_id': user_id, 'book_id': book_id})
    book = security.validate_user_book(user_id=user_id, book_id=book_id)
    return populate_genres_for_user_book(user_book=book)


def update_user_book_by_id(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4],
    title: Optional[str],
    author: Optional[str],
    synopsis: Optional[str],
    image_key: Optional[str],
    book_status_id: Optional[Union[str, uuid4]],
) -> Optional[dict]:
    """Updates a user's book using the given parameters.

    Args:
        secondary_genre_ids: [description]
        user_id: The unique ID of the user creating the book.
        book_id: The unique ID associate with the book to update.
        title: The updated title of the new book.
        author: The updated name of the person writing the book.
        synopsis: An updated short summary of the book.
        image_key: The S3 object_key associated with the user's book cover.
        book_status_id: The updated status for the book.

    Returns:
        A book populated with the updated aggregated information else None.

    Raises:
        InvalidParamException: If any of the required parameters are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(f'Updating book with id "{book_id}".')
    validate_params(func='update_user_book_by_id', params={'user_id': user_id, 'book_id': book_id})
    security.validate_user_book(user_id=user_id, book_id=book_id)

    updated_book = books_service.update_book(
        book_id=book_id,
        user_id=user_id,
        title=title,
        author=author,
        synopsis=synopsis,
        image_key=image_key,
        book_status_id=book_status_id
    )

    return populate_genres_for_user_book(user_book=updated_book)


def update_user_book_genre_by_id(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4],
    book_genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Updates a book genre with the given ID using the params passed in the body of the request.

    Args:
        user_id: The unique ID of the user pulled off of the authorized JWT.
        book_id: The unique ID of the book associated with the genre being updated.
        genre_id: The unique ID of the new genre to associate with the given book genre.
        book_genre_id: The unique ID of the book genre to update.

    Returns:
        An updated book genre else None.

    Raises:
        InvalidParamException: If any of the given parameters are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(
        f'Updating book genre with id "{book_genre_id}" to be associated with new genre '
        f'with id "{genre_id}".'
    )
    validate_params(
        func='update_user_book_genre_by_id',
        params={
            'user_id': user_id,
            'book_id': book_id,
            'genre_id': genre_id,
            'book_genre_id': book_genre_id
        }
    )
    security.validate_user_book(user_id=user_id, book_id=book_id)

    updated_book_genre = book_genres_service.update_book_genre(
        genre_id=genre_id,
        book_genre_id=book_genre_id
    )
    return book_genres_service.get_book_genre_by_id(updated_book_genre.get('id'))


def delete_user_books(user_id: Union[str, uuid4]) -> list:
    """Deletes all of the books associated with the user_id pulled from the authorized JWT.

    Args:
        user_id: The unique ID of the user pulled off of the authorized JWT.

    Returns:
        A list of all of the books that were deleted.

    Raises:
        InvalidParamException: If the given user ID is None.
    """
    log.info(f'Deleting all books for user with id "{user_id}".')
    validate_params(func='delete_user_books', params={'user_id': user_id})
    user_books = books_service.get_books(user_id)

    for user_book in user_books:
        book_genres = book_genres_service.get_book_genres(book_id=user_book.get('id'))
        for book_genre in book_genres:
            book_genres_service.delete_book_genre_by_id(book_genre_id=book_genre.get('id'))

    return books_service.delete_books(user_id=user_id)


def delete_user_book_by_id(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4]
) -> Optional[dict]:
    """Deletes the book by the given ID.

    Args:
        user_id: The unique ID of the user pulled off of the authorized JWT.
        book_id: The unique ID of the book to be deleted.

    Returns:
        The deleted book else None.

    Raises:
        InvalidParamException: If any of the required parameters are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(f'Deleting book with id "{book_id}".')
    validate_params(
        func='delete_user_book_by_id',
        params={'user_id': user_id, 'book_id': book_id}
    )
    security.validate_user_book(user_id=user_id, book_id=book_id)

    book_genres = book_genres_service.get_book_genres(book_id=book_id)
    for book_genre in book_genres:
        book_genres_service.delete_book_genre_by_id(book_genre_id=book_genre.get('id'))

    return books_service.delete_book_by_id(book_id=book_id)


def delete_secondary_book_genre(
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4],
    book_genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Deletes the secondary genre from the given book.

    Args:
        user_id: The unique ID of the user pulled off of the authorized JWT.
        book_id: The unique ID of the book to tie the new secondary genre to.
        book_genre_id: The unique ID of the book genre to delete from the book.

    Returns:
        The deleted book genre else None.

    Raises:
        InvalidParamException: If any of the required parameters are None.
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    log.info(
        f'Deleting secondary book genre with id "{book_genre_id}" from book with id "{book_id}".'
    )
    validate_params(
        func='delete_secondary_book_genre',
        params={
            'user_id': user_id,
            'book_id': book_id,
            'book_genre_id': book_genre_id
        }
    )
    security.validate_user_book(user_id=user_id, book_id=book_id)

    return book_genres_service.delete_book_genre_by_id(book_genre_id)
