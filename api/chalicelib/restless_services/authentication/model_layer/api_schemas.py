"""API schemas for the authentication service"""
# pylint: disable=too-few-public-methods
from marshmallow import fields, Schema


class GetAuthenticationQuerySchema(Schema):
    """Schema object for querying to the authentication service"""
    email = fields.String(required=True)


class PostAuthenticationBodySchema(Schema):
    """Schema object for posting to the authentication service"""
    email = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String()
