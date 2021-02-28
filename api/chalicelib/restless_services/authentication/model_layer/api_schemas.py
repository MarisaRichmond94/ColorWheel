"""API schemas for the authentication service."""
from marshmallow import fields, Schema


class GetAuthenticationQuerySchema(Schema):
    """Schema for getting authentication."""
    email = fields.String(required=True)


class PostAuthenticationBodySchema(Schema):
    """Schema for posting authentication."""
    email = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String()
