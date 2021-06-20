"""Business layer for the genres service."""
from typing import Optional, Union
from uuid import uuid4

from restful_services.genres import data
from utils.validation import validate_params


def create_genre(
    user_id: Union[str, uuid4],
    display_name: str,
    name: str,
    genre_id: Optional[Union[str, uuid4]] = None
) -> Optional[dict]:
    """Creates a new genre.

    Args:
        user_id: The FK to the users table.
        display_name: The display_name to associate with the new genre.
        name: The name to associate with the new genre.
        genre_id: The PK to assign to the new genre.

    Returns:
        A newly created genre else None.

    Raises:
        InvalidParamException: If any of the given params are None.
    """
    validate_params(
        func='create_genre',
        params={'user_id': user_id, 'display_name': display_name, 'name': name}
    )

    return data.create_genre(
        user_id=user_id,
        bucket_name=None,
        display_name=display_name,
        is_primary=False,
        name=name,
        genre_id=genre_id
    )


def get_genres(user_id: Optional[Union[str, uuid4]]) -> list:
    """Gets genres from the table filtered by given params.

    Args:
        user_id: The ID of the user to filter genres by.

    Returns:
        A list of genres filtered by any given params.
    """
    if user_id:
        return data.get_genres_by_user_id(user_id)
    return data.get_genres()


def get_genre_by_id(genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Gets a genre from the table by a given id.

    Args:
        genre_id: The PK of a genre.

    Returns:
        A genre from the table by a given id else None.

    Raises:
        InvalidParamException: If the given genre_id is None.
    """
    validate_params(func='get_genre_by_id', params={'genre_id': genre_id})
    return data.get_genre_by_id(genre_id)


def update_genre(
    name: str,
    display_name: str,
    genre_id: Union[str, uuid4]
) -> Optional[dict]:
    """Updates a genre by a given id.

    Args:
        name: The name to modify in the genre with the given id.
        display_name: The display_name to modify in the genre with the given id.
        genre_id: The PK of a genre.

    Returns:
        An updated genre with the given id else None.

    Raises:
        InvalidParamException: If any of the given params are None.
    """
    validate_params(
        func='update_genre',
        params={'name': name, 'display_name': display_name, 'genre_id': genre_id}
    )

    return data.update_genre(
        name=name,
        display_name=display_name,
        genre_id=genre_id
    )


def delete_genres(user_id: Union[str, uuid4]) -> Optional[list]:
    """Deletes genres from the table using the given params.

    Args:
        user_id: The ID of the user to delete genres by.

    Returns:
        A list of genres deleted using the given params.

    Raises:
        InvalidParamException: If any of the given params are None.
    """
    validate_params(func='delete_genres', params={'user_id': user_id})
    return data.delete_genres_by_user_id(user_id=user_id)


def delete_genre_by_id(genre_id: Union[str, uuid4]) -> Optional[dict]:
    """Deletes a genre from the table by the given id.

    Args:
        genre_id: The PK of a genre.

    Returns:
        A deleted genre with the given id else None.

    Raises:
        InvalidParamException: If the given genre_id is None.
    """
    validate_params(func='delete_genre_by_id', params={'genre_id': genre_id})
    return data.delete_genre_by_id(genre_id)
