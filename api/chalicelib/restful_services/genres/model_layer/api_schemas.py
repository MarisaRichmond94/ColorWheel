"""API schemas for the genres service."""
from marshmallow import fields, Schema


class CreateGenreBodySchema(Schema):
    """Schema for creating a new genre."""
    pass # TODO - set expected values


class GetGenresQuerySchema(Schema):
    """Schema for getting genres."""
    user_id = fields.String(required=True)


class UpdateGenreBodySchema(Schema):
    """Schema for updating a genre."""
    pass # TODO - set expected values


class DeleteGenresQuerySchema(Schema):
    """Schema for deleting genres."""
    pass # TODO - set expected values
