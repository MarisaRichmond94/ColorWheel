"""API schemas for the users service"""
# pylint: disable=too-few-public-methods
from marshmallow import fields, Schema


class CreateUserBodySchema(Schema):
    """Schema object for creating a new user"""
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
