"""Data schemas for the book_genres service."""
from marshmallow import fields, Schema, EXCLUDE

from restful_services.genres.data_schemas import GenreSchema


class BookGenreSchema(Schema):
    """Base data schema for a book_genre."""
    id = fields.UUID(required=True)
    book_id = fields.UUID(required=True, attribute='fct_book_id')
    genre_id = fields.UUID(required=True, attribute='fct_genre_id')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE


class PopulatedBookGenreSchema(Schema):
    """Populated data schema for a book_genre."""
    id = fields.UUID(required=True)
    book_id = fields.UUID(required=True, attribute='fct_book_id')
    genre = fields.Nested(GenreSchema, attribute='fct_genre')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE
