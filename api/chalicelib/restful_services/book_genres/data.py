"""Data layer for the book_genres service."""
from typing import Optional, Union
from uuid import uuid4

from db_models.fct_book_genres import FctBookGenres
from db_models.fct_genres import FctGenres
from restful_services.book_genres.data_schemas import (
    BookGenreSchema,
    PopulatedBookGenreSchema
)
from utils import db


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
    """
    with db.session_scope() as session:
        new_book_genre = FctBookGenres(
            fct_book_id=book_id,
            fct_genre_id=genre_id,
            id=book_genre_id
        )

        if new_book_genre:
            session.add(new_book_genre)
            session.commit()
            return BookGenreSchema().dump(new_book_genre)
        return None


def get_primary_genre_by_book_id(book_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets the primary book genre from the table.

    Args:
        book_id: The unique id of the book.

    Returns:
        The primary book genre else None.
    """
    with db.session_scope() as session:
        primary_book_genre = (
            session
                .query(FctBookGenres)
                .join(FctGenres)
                .filter(FctBookGenres.fct_book_id == book_id)
                .filter(FctGenres.is_primary)
                .one_or_none()
        )
        return PopulatedBookGenreSchema().dump(primary_book_genre) if primary_book_genre else None


def get_book_genres_by_book_id(book_id: Union[str, uuid4]) -> list:
    """Gets book_genres from the table by a given book.

    Args:
        book_id: The book_id to filter book_genres by.

    Returns:
        A list of book_genres with the given book_id else [].
    """
    with db.session_scope() as session:
        book_genres = session.query(FctBookGenres).filter_by(fct_book_id=book_id).all()
        return PopulatedBookGenreSchema(many=True).dump(book_genres) if book_genres else []


def get_book_genres_by_book_id_and_genre_id(
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Gets book genres from the table by a given book and genre id.

    Args:
        book_id: The book_id to filter book genres by.
        genre_id: The genre_id to filter book genres by.

    Returns:
        A book genre by the given book and genre id else None.
    """
    with db.session_scope() as session:
        book_genre = (
            session
            .query(FctBookGenres)
            .filter_by(fct_book_id=book_id, fct_genre_id=genre_id)
            .one_or_none()
        )
        return PopulatedBookGenreSchema().dump(book_genre) if book_genre else None


def get_book_genre_by_id(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a book_genre from the table by a given id.

    Args:
        book_genre_id: The PK of a book_genre.

    Returns:
        A book_genre from the table by a given id else None.
    """
    with db.session_scope() as session:
        book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()
        return PopulatedBookGenreSchema().dump(book_genre) if book_genre else None


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
    """
    with db.session_scope() as session:
        book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()

        if book_genre:
            book_genre.fct_genre_id = genre_id
            session.commit()
            return BookGenreSchema().dump(book_genre)
        return None


def delete_book_genres(book_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes book_genres from the table using the given params.

    Args:
        book_id: The FK to the book table.

    Returns:
        A list of book_genres deleted using the given params.
    """
    with db.session_scope() as session:
        book_genres = session.query(FctBookGenres).filter_by(fct_book_id=book_id,).all()

        if book_genres:
            for book_genre in book_genres:
                session.delete(book_genre)
                session.commit()
            return BookGenreSchema(many=True).dump(book_genres)
        return []


def delete_book_genre_by_id(book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a book_genre from the table by the given id.

    Args:
        book_genre_id: The PK of a book_genre.

    Returns:
        A deleted book_genre with the given id else None.
    """
    with db.session_scope() as session:
        book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()

    if book_genre:
        session.delete(book_genre)
        session.commit()
        return BookGenreSchema().dump(book_genre)
    return None
