"""Data schemas for the genres service."""
from marshmallow import fields, Schema, EXCLUDE

from restful_services.users.data_schemas import UserSchema


class GenreSchema(Schema):
    """Base data schema for a genre."""
    id = fields.UUID(required=True)
    bucket_name = fields.String(required=True)
    display_name = fields.String(required=True)
    is_primary = fields.Boolean(required=True)
    name = fields.String(required=True)
    user_id = fields.UUID(required=True, attribute='dim_user_id')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE


class PopulatedGenreSchema(Schema):
    """Populated data schema for a genre."""
    id = fields.UUID(required=True)
    bucket_name = fields.String(required=True)
    display_name = fields.String(required=True)
    is_primary = fields.Boolean(required=True)
    name = fields.String(required=True)
    user = fields.Nested(UserSchema, attribute='dim_user')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE
