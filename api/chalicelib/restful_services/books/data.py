"""Data layer for the books service."""
# pylint: disable=too-many-arguments
import datetime
from typing import Optional, Union
from uuid import uuid4

from db_models.fct_books import FctBooks
from restful_services.books.data_schemas import (
    BookSchema,
    PopulatedBookSchema
)
from utils import db


def create_book(
    book_status_id: Union[str, uuid4],
    user_id: Union[str, uuid4],
    author: str,
    image_key: Optional[str],
    summary: Optional[str],
    timestamp: datetime,
    title: str,
    book_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new book.

    Args:
        book_status_id: The FK to the book_statuses table.
        user_id: The FK to the users table.
        author: The author to associate with the new book.
        image_key: The image_key to associate with the new book.
        summary: The summary to associate with the new book.
        timestamp: The timestamp to associate with the new book.
        title: The title to associate with the new book.
        book_id: The PK to assign to the new book.

    Returns:
        A newly created book else None.
    """
    with db.session_scope() as session:
        new_book = FctBooks(
            dim_book_status_id=book_status_id,
            dim_user_id=user_id,
            author=author,
            image_key=image_key,
            summary=summary,
            timestamp=timestamp,
            title=title,
            id=book_id
        )

        if new_book:
            session.add(new_book)
            session.commit()
            return BookSchema().dump(new_book)
        return None


def get_books() -> list:
    """Gets books from the table filtered by given params.

    Returns:
        A list of books filtered by any given params.
    """
    with db.session_scope() as session:
        books = session.query(FctBooks).all()
        return PopulatedBookSchema(many=True).dump(books) if books else []


def get_books_by_user_id(user_id: Union[str, uuid4]) -> list:
    """Gets books from the table by a given user.

    Args:
        user_id: The user_id to filter books by.

    Returns:
        A list of books with the given user_id else [].
    """
    with db.session_scope() as session:
        books = session.query(FctBooks).filter_by(dim_user_id=user_id).all()
        return PopulatedBookSchema(many=True).dump(books) if books else []


def get_book_by_title_and_user_id(title: str, user_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets books from the table by a given user.

    Args:
        title: The title of the book to filter books by.
        user_id: The user_id to filter books by.

    Returns:
        A book with the given title user_id else None.
    """
    with db.session_scope() as session:
        book = session.query(FctBooks).filter_by(title=title, dim_user_id=user_id).one_or_none()
        return PopulatedBookSchema().dump(book) if book else None


def get_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a book from the table by a given id.

    Args:
        book_id: The PK of a book.

    Returns:
        A book from the table by a given id else None.
    """
    with db.session_scope() as session:
        book = session.query(FctBooks).filter_by(id=book_id).one_or_none()
        return PopulatedBookSchema().dump(book) if book else None


def update_book(
    book_id: Union[str, uuid4],
    title: Optional[str] = None,
    author: Optional[str] = None,
    summary: Optional[str] = None,
    image_key: Optional[str] = None,
    book_status_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Updates a book by a given id.

    Args:
        book_id: The PK of a book.
        title: The title to modify in the book with the given id.
        author: The author to modify in the book with the given id.
        summary: The summary to modify in the book with the given id.
        image_key: The image_key to modify in the book with the given id.
        book_status_id: The FK to the book_status table.

    Returns:
        An updated book with the given id else None.
    """
    with db.session_scope() as session:
        book = session.query(FctBooks).filter_by(id=book_id).one_or_none()

        if book:
            book.title = title if title else book.title
            book.author = author if author else book.author
            book.summary = summary if summary else book.summary
            book.image_key = image_key if image_key else book.image_key
            book.dim_book_status_id = book_status_id if book_status_id else book.dim_book_status_id
            session.commit()
            return BookSchema().dump(book)
        return None


def delete_books(user_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes books from the table using the given params.

    Args:
        user_id: The FK to the user table.

    Returns:
        A list of books deleted using the given params.
    """
    with db.session_scope() as session:
        books = session.query(FctBooks).filter_by(dim_user_id=user_id,).all()

        if books:
            for book in books:
                session.delete(book)
                session.commit()
            return BookSchema(many=True).dump(books)
        return []


def delete_book_by_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a book from the table by the given id.

    Args:
        book_id: The PK of a book.

    Returns:
        A deleted book with the given id else None.
    """
    with db.session_scope() as session:
        book = session.query(FctBooks).filter_by(id=book_id).one_or_none()

    if book:
        session.delete(book)
        session.commit()
        return BookSchema().dump(book)
    return None
