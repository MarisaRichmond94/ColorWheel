"""API schemas for the book_management service."""
from marshmallow import fields, Schema


class CreateBookBodySchema(Schema):
    """POST book body schema for book management."""
    author = fields.String(required=True)
    title = fields.String(required=True)
    primary_genre_id = fields.UUID(required=True)
    image_key = fields.String(required=False)
    synopsis = fields.String(required=False)
    secondary_genre_names = fields.List(fields.String, required=False)
    book_id = fields.UUID(required=False)


class CreateBookGenreBodySchema(Schema):
    """POST book genre body schema for book management."""
    book_id = fields.UUID(required=False)
    secondary_genre_name = fields.String(required=True)


class DeleteBookGenresQuerySchema(Schema):
    """DELETE book genre query schema for book management."""
    book_id = fields.UUID(required=True)


class UpdateBookBodySchema(Schema):
    """PATCH book body schema for book management."""
    title = fields.String(required=False)
    author = fields.String(required=False)
    synopsis = fields.String(required=False)
    image_key = fields.String(required=False)
    book_status_id = fields.UUID(required=False)


class UpdateBookGenreBodySchema(Schema):
    """PATCH book genre body schema for book management."""
    book_id = fields.UUID(required=True)
    genre_name = fields.String(required=True)
