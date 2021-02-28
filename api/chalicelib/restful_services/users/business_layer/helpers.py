"""Helpers for the users service."""
import bcrypt
from loguru import logger as log


def generate_hashed_password(password: str) -> bytes:
    """Generates a hashed and salted binary string using the given plain text password and a
        randomly generated salt

    Args:
        password - A plain text string of at least 10 characters.

    Returns:
        A hashed and salted byte string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def validate_password(
    password: str,
    hashed: str,
) -> bool:
    """Validates that a plain text password matches the hashed and salted binary string associated
        with a user entity.

    Args:
        password - A plain text string of at least 10 characters.
        hashed - A binary string that has been hashed and salted.

    Returns:
        True if the give password and hashes match else False.
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except ValueError as invalid_password_exception:
        log.exception(invalid_password_exception)
        return False
