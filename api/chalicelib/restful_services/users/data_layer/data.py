"""Data layer for the users service"""
from typing import Dict, Optional, Union
from uuid import uuid4

from db_models.dim_users import DimUsers
from libs import db
from restful_services.users.model_layer.data_schemas import UserSchema


def create_user(name: str, email: str, password: str) -> Optional[Dict]:
    """Creates new user in the dim_users table

    Args:
        name: The first and last name of the new user
        email: The email to associate with the new user
        password: The secret string need to generate a hash/salt combo to validate a user's identity

    Returns:
        JSON representation of a newly created user from the dim_users table or None
    """
    with db.session_scope() as session:
        user = DimUsers(
            name=name,
            email=email,
            password=password
        )

        if user:
            session.add(user)
            session.commit()
            return UserSchema().dump(user)

        return None


def get_user_by_id(user_id: Union[str, uuid4]) -> Optional[Dict]:
    """Gets user from the dim_users table by id

    Args:
        user_id: The primary key for a user in the dim_users table

    Returns:
        JSON representation of a user from the database with matching user_id or None
    """
    with db.session_scope() as session:
        user = session.query(DimUsers).filter_by(id=user_id).one_or_none()
        return UserSchema().dump(user) if user else None
