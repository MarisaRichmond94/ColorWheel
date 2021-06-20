"""API schemas for the genres service."""
from marshmallow import fields, Schema


class CreateGenreBodySchema(Schema):
    """Schema for creating a new genre."""
    id = fields.UUID(required=False)
    display_name = fields.String(required=True)
    name = fields.String(required=True)
    user_id = fields.UUID(required=True)


class GetGenresQuerySchema(Schema):
    """Schema for getting genres."""
    user_id = fields.UUID(required=False)


class UpdateGenreBodySchema(Schema):
    """Schema for updating a genre."""
    name = fields.String(required=True)
    display_name = fields.String(required=True)


class DeleteGenresQuerySchema(Schema):
    """Schema for deleting genres."""
    user_id = fields.UUID(required=True)
