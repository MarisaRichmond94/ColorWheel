"""Helper file for security functionality related to the book management service."""
from typing import Optional, Union
from uuid import uuid4

from exceptions.restless_service import UnauthorizedAccessException
from restful_services.books import business as books_service


def validate_user_book(
    session: any,
    user_id: Union[str, uuid4],
    book_id: Union[str, uuid4],
) -> Optional[dict]:
    """Verifies that the user is authorized to access the given book.

    Args:
        session: The current database session for the request.
        user_id: The unique ID of the user pulled off of the authorized JWT.
        book_id: The unique ID of the book being accessed by the given user.

    Returns:
        The authorized book else None.

    Raises:
        UnauthorizedAccessException: If the user ID associated with the book does not match the user
            ID pulled from the request's JWT.
    """
    user_book = books_service.get_book_by_id(session, book_id=book_id)
    if user_book.get('user', {}).get('id') != user_id:
        raise UnauthorizedAccessException(
            accessing_user_id=user_id,
            data=user_book,
            authorized_user_id=user_book.get('user', {}).get('id')
        )

    return user_book
