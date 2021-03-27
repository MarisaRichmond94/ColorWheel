"""Data schemas for the sessions service."""
from marshmallow import fields, Schema, EXCLUDE

from restful_services.users.model_layer.data_schemas import UserSchema

class SessionSchema(Schema):
    """Base data schema for a session."""
    id = fields.UUID(required=True)
    user_id = fields.UUID(required=True, attribute='dim_user_id')
    token = fields.Str(required=True)
    datetime = fields.DateTime(required=True)

    class Meta:
        """Meta class."""
        unknown = EXCLUDE


class PopulatedSessionSchema(Schema):
    """Populated data schema for a session."""
    id = fields.UUID(required=True)
    user = fields.Nested(UserSchema, attribute='dim_user')
    token = fields.Str(required=True)
    datetime = fields.DateTime(required=True)

    class Meta:
        """Meta class."""
        unknown = EXCLUDE
