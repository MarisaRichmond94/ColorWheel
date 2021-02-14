import bcrypt
from loguru import logger as log


def generate_hashed_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def validate_password(password: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except ValueError as invalid_password_exception:
        log.exception(invalid_password_exception)
        return False
