"""API layer for the genres service."""
from typing import Optional

from chalice import Blueprint

from restful_services.genres import business
from restful_services.genres.api_schemas import (
    CreateGenreBodySchema,
    DeleteGenresQuerySchema,
    GetGenresQuerySchema,
    UpdateGenreBodySchema
)
from utils.api_handler import api_handler

api = Blueprint(__name__)
ROUTE = '/genres'
ENTITY_ID = '/{genre_id}'


@api_handler(
    api,
    path=ROUTE,
    methods=['POST'],
    body_schema=CreateGenreBodySchema)
def create_genre() -> Optional[dict]:
    """Creates a new genre in the table.

    Returns:
        A newly created genre else None.
    """
    return business.create_genre(
        user_id=api.handled_request.body.get('user_id'),
        display_name=api.handled_request.body.get('display_name'),
        name=api.handled_request.body.get('name'),
        genre_id=api.handled_request.body.get('id')
    )


@api_handler(
    api,
    path=ROUTE,
    methods=['GET'],
    query_schema=GetGenresQuerySchema)
def get_genres() -> list:
    """Gets genres from the table filtered by given params.

    Returns:
        A list of genres filtered by any given params.
    """
    return business.get_genres(user_id=api.handled_request.query.get('user_id'))


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['GET'])
def get_genre_by_id(genre_id: str) -> Optional[dict]:
    """Gets a genre from the table by a given id.

    Args:
        genre_id: The primary key of a genre.

    Returns:
        A genre from the table by a given id else None.
    """
    return business.get_genre_by_id(genre_id)


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['PATCH'],
    body_schema=UpdateGenreBodySchema)
def update_genre(genre_id: str) -> Optional[dict]:
    """Updates a genre in the table by a given id.

    Args:
        genre_id: The primary key of a genre.

    Returns:
        An updated genre with the given id else None.
    """
    return business.update_genre(
        name=api.handled_request.body.get('name'),
        display_name=api.handled_request.body.get('display_name'),
        genre_id=genre_id
    )


@api_handler(
    api,
    path=ROUTE,
    methods=['DELETE'],
    query_schema=DeleteGenresQuerySchema)
def delete_genres() -> Optional[list]:
    """Deletes genres from the table using the given params.

    Returns:
        A list of genres deleted using the given params.
    """
    return business.delete_genres(
        user_id=api.handled_request.query.get('user_id')
    )


@api_handler(
    api,
    path=f'{ROUTE}{ENTITY_ID}',
    methods=['DELETE'])
def delete_genre_by_id(genre_id: str) -> Optional[dict]:
    """Deletes a genre from the table by the given id.

    Args:
        genre_id: The primary key of a genre.

    Returns:
        A deleted genre with the given id else None.
    """
    return business.delete_genre_by_id(genre_id)
