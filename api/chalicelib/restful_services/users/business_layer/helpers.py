import bcrypt


def generate_hashed_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed, salt


def validate_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password, hashed)
