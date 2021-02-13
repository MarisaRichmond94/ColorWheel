from marshmallow import fields, Schema, EXCLUDE

from restful_services.users.model_layer.data_schemas import UserSchema

class SessionSchema(Schema):
    """Data schema for a user"""
    id = fields.UUID(required=True)
    user_id = fields.UUID(required=True, attribute='dim_user_id')
    token = fields.Str(required=True)
    datetime = fields.DateTime(required=True)

    class Meta:
        unknown = EXCLUDE


class PopulatedSessionSchema(Schema):
    """Data schema for a user"""
    id = fields.UUID(required=True)
    user = fields.Nested(UserSchema, attribute='dim_user')
    token = fields.Str(required=True)
    datetime = fields.DateTime(required=True)

    class Meta:
        unknown = EXCLUDE
