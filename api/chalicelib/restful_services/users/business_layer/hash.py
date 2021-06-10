"""Hash helper functions for the users service."""
import bcrypt


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
