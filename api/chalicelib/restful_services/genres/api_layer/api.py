"""API layer for the genres service."""
from typing import Optional

from chalice import Blueprint

from restful_services.genres.business_layer import business
from restful_services.genres.model_layer.api_schemas import (
    CreateGenreBodySchema,
    GetGenresQuerySchema,
    UpdateGenreBodySchema,
    DeleteGenresQuerySchema,
)
from utils.api_handler import api_handler

api = Blueprint(__name__)


@api_handler(
    api=api,
    path="/genres",
    methods=["POST"],
    body_schema=CreateGenreBodySchema,
)
def create_genre() -> Optional[dict]:
    """Creates a new genre in the fct_genres table.

    Returns:
        A newly created genre else None.
    """
    return business.create_genre(
        # pass in variables
    )


@api_handler(
    api=api,
    path="/genres",
    methods=["GET"],
    query_schema=GetGenresQuerySchema,
)
def get_genres() -> list:
    """Gets genres from the fct_genres table filtered by given params.

    Returns:
        A list of genres filtered by any given params.
    """
    return business.get_genres(
        # pass in variables
    )


@api_handler(
    api=api,
    path="/genres/{genre_id}",
    methods=["PATCH"],
    body_schema=UpdateGenreBodySchema,
)
def update_genre(genre_id: str) -> Optional[dict]:
    """Updates a genre in the fct_genres table by the given id.

    Args:
        genre_id - The primary key of a genre in the fct_genres table.

    Returns:
        An updated genre with the given id else None.
    """
    return business.update_genre(
        genre_id=genre_id,
        # pass in variables
    )


@api_handler(
    api=api,
    path="/genres",
    methods=["DELETE"],
    query_schema=DeleteGenresQuerySchema,
)
def delete_genres() -> list:
    """Deletes genres from the fct_genres table using given params.

    Returns:
        A list of genres deleted using given params.
    """
    return business.delete_genres(
        # pass in variables
    )


@api_handler(
    api=api,
    path="/genres/{genre_id}",
    methods=["DELETE"],
)
def delete_genre_by_id(genre_id: str) -> Optional[dict]:
    """Deletes a genre from the fct_genres table by the given id.

    Args:
        genre_id - The primary key of a genre in the fct_genres table.

    Returns:
        A deleted genre with the given id else None.
    """
    return business.delete_genre_by_id(genre_id=genre_id)
