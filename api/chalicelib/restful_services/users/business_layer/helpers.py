import bcrypt


def generate_hashed_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt), salt


def validate_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password, hashed)
