"""Data schemas for the books service."""
from marshmallow import fields, Schema, EXCLUDE

from restful_services.book_statuses.data_schemas import BookStatusSchema
from restful_services.users.data_schemas import UserSchema


class BookSchema(Schema):
    """Base data schema for a book."""
    id = fields.UUID(required=True)
    author = fields.String(required=True)
    image_key = fields.String(required=True)
    summary = fields.String(required=True)
    timestamp = fields.DateTime(required=True)
    title = fields.String(required=True)
    book_status_id = fields.UUID(required=True, attribute='dim_book_status_id')
    user_id = fields.UUID(required=True, attribute='dim_user_id')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE


class PopulatedBookSchema(Schema):
    """Populated data schema for a book."""
    id = fields.UUID(required=True)
    author = fields.String(required=True)
    image_key = fields.String(required=True)
    summary = fields.String(required=True)
    timestamp = fields.DateTime(required=True)
    title = fields.String(required=True)
    book_status = fields.Nested(BookStatusSchema, attribute='dim_book_status')
    user = fields.Nested(UserSchema, attribute='dim_user')

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE
