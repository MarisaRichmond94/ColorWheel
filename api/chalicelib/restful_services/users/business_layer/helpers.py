"""Helper functions for the users service"""
import bcrypt

from libs.validation import validate_params


def generate_hashed_password(password: str) -> str:
    """Generates a salt using bcrypt and then hashes the given password using the generated salt

    Args:
        password - The secret string that will be used to validate a user's identity

    Returns:
        A hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt), salt


def validate_password(password: str, hash: str) -> bool:
    """Validates a given password against a hashed password

    Args:
        password - The raw secret string used to validate a user's identity

    Returns:
        True or False
    """
    return bcrypt.checkpw(password, hash)
