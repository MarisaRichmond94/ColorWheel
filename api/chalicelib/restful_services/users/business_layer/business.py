from typing import Optional

from utils.validation import validate_params
from restful_services.users.data_layer import data
from restful_services.users.business_layer.helpers import generate_hashed_password


def create_user(name: str, email: str, password: str) -> Optional[dict]:
    validate_params(
        func="create_user",
        params={"name": name, "email": email, "password": password}
    )

    hashed_password = generate_hashed_password(password=password)
    return data.create_user(name=name, email=email, password=hashed_password)


def get_user_by_email(email: str) -> Optional[dict]:
    validate_params(func="get_user_by_email", params={"email": email})
    return data.get_user_by_email(email=email)
