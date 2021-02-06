# pylint: disable=too-few-public-methods
from marshmallow import fields, Schema


class GetAuthenticationQuerySchema(Schema):
    email = fields.String(required=True)


class PostAuthenticationBodySchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String()
