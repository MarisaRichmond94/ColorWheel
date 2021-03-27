"""Data layer for the genres service."""
from typing import Optional

from db_models.fct_genres import FctGenres
from utils import db
from utils.types import UUIDType
from restful_services.genres.model_layer.data_schemas import (
    GenresSchema,
    PopulatedGenresSchema,
)


def create_genre(
    # pass in variables
) -> Optional[dict]:
    """Creates a new genre in the fct_genres table.

    Args:
        # list any given params here

    Returns:
        A newly created genre else None.
    """
    with db.session_scope() as session:
        new_genre = FctGenres(
            # pass in variables
        )

        if new_genre:
            session.add(new_genre)
            session.commit()
            return GenresSchema().dump(new_genre)
        return None


def get_genres() -> list:
    """Gets all genres from the fct_genres table.

    Returns:
        A list of genres.
    """
    with db.session_scope() as session:
        genres = session.query(FctGenres).all()
        return PopulatedGenresSchema(many=True).dump(genres) if genres else []


def update_genre(
    genre_id: UUIDType,
    # pass any other given params
) -> Optional[dict]:
    """Updates a genre in the fct_genres table by the given id.

    Args:
        genre_id - The primary key of a genre in the fct_genres table.
        # list any other given params here

    Returns:
        An updated genre with the given id else None.
    """
    with db.session_scope() as session:
        genre = session.query(FctGenres).filter_by(id=genre_id).one_or_none()

        if genre:
            # update entity
            session.commit()
            return GenresSchema().dump(genre)
        return None


def delete_genres(
    # pass any given params
) -> list:
    """Deletes genres from the fct_genres table using given params.

    Args:
        # list any given params here

    Returns:
        A list of genres deleted using given params.
    """
    with db.session_scope() as session:
        genres = session.query(FctGenres).filter_by().all()

        if genres:
            for genre in genres:
                session.delete(genre)
                session.commit()
                return GenresSchema(many=True).dump(genres)
        return []


def delete_genre_by_id(genre_id: UUIDType) -> Optional[dict]:
    """Deletes a genre from the fct_genres table by the given id.

    Args:
        genre_id - The primary key of a genre in the fct_genres table.

    Returns:
        A deleted genre with the given id else None.
    """
    with db.session_scope() as session:
        genre = session.query(FctGenres).filter_by(id=genre_id).one_or_none()

        if genre:
            session.delete(genre)
            session.commit()
            return GenresSchema().dump(genre)
        return None
