"""Business layer for the genres service."""
from typing import Optional

from utils.types import UUIDType
from utils.validation import validate_params
from restful_services.genres.data_layer import data


def create_genre(
    # pass in variables
) -> Optional[dict]:
    """Creates a new genre in the fct_genres table.

    Args:
        # list any given params here

    Returns:
        A newly created genre else None.

    Raises:
        InvalidParamException - If any of the given params are None.
    """
    validate_params(
        func='create_genre',
        params={
            # pass required params here
        },
    )
    return data.create_genre(
        # pass in variables
    )


def get_genres(
    # pass in variables
) -> list:
    """Gets genres from the fct_genres table filtered by given params.

    Args:
        # list any given params here

    Returns:
        A list of genres filtered by any given params.
    """
    return data.get_genres()


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

    Raises:
        InvalidParamException - If any of the given params or the genre_id is None.
    """
    validate_params(
        func='update_genre',
        params={
            'genre_id': genre_id,
            # pass other required params here
        }
    )
    return data.update_genre(
        genre_id=genre_id,
        # pass any other given params
    )


def delete_genres(
    # pass any given params
) -> list:
    """Deletes genres from the fct_genres table using given params.

    Args:
        # list any given params here

    Returns:
        A list of genres deleted using given params.
    """
    return data.delete_genres(
        # pass any other given params
    )


def delete_genre_by_id(genre_id: UUIDType) -> Optional[dict]:
    """Deletes a genre from the fct_genres table by the given id.

    Args:
        genre_id - The primary key of a genre in the fct_genres table.

    Returns:
        A deleted genre with the given id else None.

    Raises:
        InvalidParamException - If the given genre_id is None.
    """
    validate_params(
        func='delete_genre_by_id',
        params={'genre_id': genre_id},
    )
    return data.delete_genre_by_id(genre_id=genre_id)
