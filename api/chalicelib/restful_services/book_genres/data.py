"""Data layer for the book_genres service."""
from typing import Optional, Union
from uuid import uuid4

from db_models.fct_book_genres import FctBookGenres
from db_models.fct_genres import FctGenres
from restful_services.book_genres.data_schemas import (
    BookGenreSchema,
    PopulatedBookGenreSchema
)


def create_book_genre(
    session: any,
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4],
    book_genre_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new book_genre.

    Args:
        session: The current database session.
        book_id: The FK to the books table.
        genre_id: The FK to the genres table.
        book_genre_id: The PK to assign to the new book_genre.

    Returns:
        A newly created book_genre else None.
    """
    new_book_genre = FctBookGenres(
        fct_book_id=book_id,
        fct_genre_id=genre_id,
        id=book_genre_id or uuid4()
    )

    if new_book_genre:
        session.add(new_book_genre)
        return BookGenreSchema().dump(new_book_genre)
    return None


def get_primary_genre_by_book_id(session: any, book_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets the primary book genre from the table.

    Args:
        session: The current database session.
        book_id: The unique id of the book.

    Returns:
        The primary book genre else None.
    """
    primary_book_genre = (
        session
            .query(FctBookGenres)
            .join(FctGenres)
            .filter(FctBookGenres.fct_book_id == book_id)
            .filter(FctGenres.is_primary)
            .one_or_none()
    )
    return PopulatedBookGenreSchema().dump(primary_book_genre) if primary_book_genre else None


def get_book_genres_by_book_id(session: any, book_id: Union[str, uuid4]) -> list:
    """Gets book_genres from the table by a given book ID.

    Args:
        session: The current database session.
        book_id: The book_id to filter book_genres by.

    Returns:
        A list of book_genres with the given book_id else [].
    """
    book_genres = session.query(FctBookGenres).filter_by(fct_book_id=book_id).all()
    return PopulatedBookGenreSchema(many=True).dump(book_genres) if book_genres else []


def get_book_genres_by_genre_id(session: any, genre_id: Union[str, uuid4]) -> list:
    """Gets book_genres from the table by a given genre ID.

    Args:
        session: The current database session.
        genre_id: The genre_id to filter book_genres by.

    Returns:
        A list of book_genres with the given genre_id else [].
    """
    book_genres = session.query(FctBookGenres).filter_by(dim_genre_id=genre_id).all()
    return PopulatedBookGenreSchema(many=True).dump(book_genres) if book_genres else []


def get_book_genres_by_book_id_and_genre_id(
    session: any,
    book_id: Union[str, uuid4],
    genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Gets book genres from the table by a given book and genre id.

    Args:
        session: The current database session.
        book_id: The book_id to filter book genres by.
        genre_id: The genre_id to filter book genres by.

    Returns:
        A book genre by the given book and genre id else None.
    """
    book_genre = (
        session
        .query(FctBookGenres)
        .filter_by(fct_book_id=book_id, fct_genre_id=genre_id)
        .one_or_none()
    )
    return PopulatedBookGenreSchema().dump(book_genre) if book_genre else None


def get_book_genre_by_id(session: any, book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a book_genre from the table by a given id.

    Args:
        session: The current database session.
        book_genre_id: The PK of a book_genre.

    Returns:
        A book_genre from the table by a given id else None.
    """
    book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()
    return PopulatedBookGenreSchema().dump(book_genre) if book_genre else None


def update_book_genre(
    session: any,
    genre_id: Union[str, uuid4],
    book_genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Updates a book_genre by a given id.

    Args:
        session: The current database session.
        genre_id: The FK to the genre table.
        book_genre_id: The PK of a book_genre.

    Returns:
        An updated book_genre with the given id else None.
    """
    book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()

    if book_genre:
        book_genre.fct_genre_id = genre_id
        return BookGenreSchema().dump(book_genre)
    return None


def delete_book_genres(session: any, book_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes book_genres from the table using the given params.

    Args:
        session: The current database session.
        book_id: The FK to the book table.

    Returns:
        A list of book_genres deleted using the given params.
    """
    book_genres = session.query(FctBookGenres).filter_by(fct_book_id=book_id,).all()

    if book_genres:
        for book_genre in book_genres:
            session.delete(book_genre)
        return BookGenreSchema(many=True).dump(book_genres)
    return []


def delete_book_genre_by_id(session: any, book_genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a book_genre from the table by the given id.

    Args:
        session: The current database session.
        book_genre_id: The PK of a book_genre.

    Returns:
        A deleted book_genre with the given id else None.
    """
    book_genre = session.query(FctBookGenres).filter_by(id=book_genre_id).one_or_none()

    if book_genre:
        session.delete(book_genre)
        return BookGenreSchema().dump(book_genre)
    return None
