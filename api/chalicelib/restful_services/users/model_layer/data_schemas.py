"""Data schemas for the users service."""
from marshmallow import fields, Schema, EXCLUDE

class UserSchema(Schema):
    """Base data schema for a user."""
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        """Meta class."""
        unknown = EXCLUDE
