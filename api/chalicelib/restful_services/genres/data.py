"""Data layer for the genres service."""
# pylint: disable=too-many-arguments
from typing import Optional, Union
from uuid import uuid4

from db_models.fct_genres import FctGenres
from restful_services.genres.data_schemas import GenreSchema, PopulatedGenreSchema
from utils.alembic.fixtures.users import DEFAULT_USER_ID
from utils import db


def create_genre(
    user_id: Union[str, uuid4],
    bucket_name: Optional[str],
    display_name: str,
    is_primary: bool,
    name: str,
    genre_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new genre.

    Args:
        user_id: The FK to the users table.
        bucket_name: The bucket_name to associate with the new genre.
        display_name: The display_name to associate with the new genre.
        is_primary: The is_primary to associate with the new genre.
        name: The name to associate with the new genre.
        genre_id: The PK to assign to the new genre.

    Returns:
        A newly created genre else None.
    """
    new_genre = FctGenres(
        dim_user_id=user_id,
        bucket_name=bucket_name,
        display_name=display_name,
        is_primary=is_primary,
        name=name,
        id=genre_id or uuid4()
    )

    if new_genre:
        db.SESSION.add(new_genre)
        return GenreSchema().dump(new_genre)
    return None


def get_genres() -> list:
    """Gets genres from the table filtered by given params.

    Returns:
        A list of genres filtered by any given params.
    """
    genres = db.SESSION.query(FctGenres).all()
    return PopulatedGenreSchema(many=True).dump(genres) if genres else []


def get_genres_by_user_id(user_id: Union[str, uuid4]) -> list:
    """Gets genres from the table by a given user_id.

    Args:
        user_id: The ID of the user to filter genres by.

    Returns:
        A list of genres with the given user else [].
    """
    genres = (
        db.SESSION
            .query(FctGenres)
            .filter(FctGenres.dim_user_id.in_([user_id, DEFAULT_USER_ID]))
            .all()
    )
    return PopulatedGenreSchema(many=True).dump(genres) if genres else []


def get_genre_by_display_name_and_user_id(
    display_name: str,
    user_id: Union[str, uuid4]
) -> Optional[dict]:
    """Gets a genre by a given name.

    Args:
        display_name: The unique name of the genre.
        user_id: The ID of the user to filter genres by.

    Returns:
        A genre by the given name else None.
    """
    genre = (
        db.SESSION
            .query(FctGenres)
            .filter(FctGenres.display_name == display_name)
            .filter(FctGenres.dim_user_id.in_([user_id, DEFAULT_USER_ID]))
            .one_or_none()
    )
    return PopulatedGenreSchema().dump(genre) if genre else None


def get_genre_by_id(genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a genre from the table by a given id.

    Args:
        genre_id: The PK of a genre.

    Returns:
        A genre from the table by a given id else None.
    """
    genre = db.SESSION.query(FctGenres).filter_by(id=genre_id).one_or_none()
    return PopulatedGenreSchema().dump(genre) if genre else None


def update_genre(name: str, display_name: str, genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Updates a genre by a given id.

    Args:
        name: The name to modify in the genre with the given id.
        display_name: The display_name to modify in the genre with the given id.
        genre_id: The PK of a genre.

    Returns:
        An updated genre with the given id else None.
    """
    genre = db.SESSION.query(FctGenres).filter_by(id=genre_id).one_or_none()

    if genre:
        genre.name = name
        genre.display_name = display_name
        return GenreSchema().dump(genre)
    return None


def delete_genres_by_user_id(user_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes genres from the table using the given params.

    Args:
        user_id: The ID of the user to delete genres by.

    Returns:
        A list of genres deleted using the given params.
    """
    genres = db.SESSION.query(FctGenres).filter_by(dim_user_id=user_id).all()

    if genres:
        for genre in genres:
            db.SESSION.delete(genre)
        return GenreSchema(many=True).dump(genres)
    return []


def delete_genre_by_id(genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a genre from the table by the given id.

    Args:
        genre_id: The PK of a genre.

    Returns:
        A deleted genre with the given id else None.
    """
    genre = db.SESSION.query(FctGenres).filter_by(id=genre_id).one_or_none()

    if genre:
        db.SESSION.delete(genre)
        return GenreSchema().dump(genre)
    return None
