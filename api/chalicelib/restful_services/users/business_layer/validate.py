"""Validation helper functions for the users service."""
import bcrypt
from loguru import logger as log


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
