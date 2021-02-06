from marshmallow import fields, Schema, EXCLUDE

class UserSchema(Schema):
    """Data schema for a user"""
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
