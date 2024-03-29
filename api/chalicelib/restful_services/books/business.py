"""Business layer for the books service."""
# pylint: disable=too-many-arguments
from datetime import datetime
from typing import Optional, Union
from uuid import uuid4

import pytz

from restful_services.books import data
from settings.restful_services import INITIAL_BOOK_STATUS_ID
from utils.validation import validate_entity_is_unique, validate_params


def create_book(
    user_id: Union[str, uuid4],
    author: str,
    title: str,
    image_key: Optional[str] = None,
    synopsis: Optional[str] = None,
    book_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new book.

    Args:
        user_id: The FK to the users table.
        author: The author to associate with the new book.
        image_key: The image_key to associate with the new book.
        synopsis: The synopsis to associate with the new book.
        title: The title to associate with the new book.
        book_id: The PK to assign to the new book.

    Returns:
        A newly created book else None.

    Raises:
        InvalidParamException: If any of the given params are None.
        UniqueEntityException: If a title/user_id match already exists in the table.
    """
    validate_params(
        func='create_book',
        params={'user_id': user_id, 'author': author, 'title': title}
    )
    validate_entity_is_unique(
        func=data.get_book_by_title_and_user_id,
        title=title,
        user_id=user_id
    )

    return data.create_book(
        book_status_id=INITIAL_BOOK_STATUS_ID,
        user_id=user_id,
        author=author,
        image_key=image_key,
        synopsis=synopsis,
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        title=title,
        book_id=book_id
    )


def get_books(user_id: Optional[Union[str, uuid4]] = None) -> list:
    """Gets books from the table filtered by given params.

    Args:
        user_id: The FK to the user table.

    Returns:
        A list of books filtered by any given params.
    """
    if user_id:
        return data.get_books_by_user_id(user_id=user_id)
    return data.get_books()


def get_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a book from the table by a given id.

    Args:
        book_id: The PK of a book.

    Returns:
        A book from the table by a given id else None.

    Raises:
        InvalidParamException: If the given book_id is None.
    """
    validate_params(func='get_book_by_id', params={'book_id': book_id})
    return data.get_book_by_id(book_id=book_id)


def update_book(
    book_id: Union[str, uuid4],
    user_id: Union[str, uuid4],
    title: Optional[str] = None,
    author: Optional[str] = None,
    synopsis: Optional[str] = None,
    image_key: Optional[str] = None,
    book_status_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Updates a book by a given id.

    Args:
        book_id: The PK of a book.
        title: The title to modify in the book with the given id.
        author: The author to modify in the book with the given id.
        synopsis: The synopsis to modify in the book with the given id.
        image_key: The image_key to modify in the book with the given id.
        book_status_id: The FK to the book_status table.

    Returns:
        An updated book with the given id else None.

    Raises:
        InvalidParamException: If any of the given params are None.
        UniqueEntityException: If a title/user_id match already exists in the table.
    """
    validate_params(func='update_book', params={'book_id': book_id})
    if title:
        validate_entity_is_unique(
            func=data.get_book_by_title_and_user_id,
            title=title,
            user_id=user_id
        )

    return data.update_book(
        book_id=book_id,
        title=title,
        author=author,
        synopsis=synopsis,
        image_key=image_key,
        book_status_id=book_status_id
    )


def delete_books(user_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes books from the table using the given params.

    Args:
        user_id: The FK to the user table.

    Returns:
        A list of books deleted using the given params.

    Raises:
        InvalidParamException: If any of the given params are None.
    """
    validate_params(func='delete_books', params={'user_id': user_id})
    return data.delete_books(user_id=user_id)


def delete_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a book from the table by the given id.

    Args:
        book_id: The PK of a book.

    Returns:
        A deleted book with the given id else None.

    Raises:
        InvalidParamException: If the given book_id is None.
    """
    validate_params(func='delete_book_by_id', params={'book_id': book_id})
    return data.delete_book_by_id(book_id=book_id)
