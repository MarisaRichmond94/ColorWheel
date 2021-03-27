"""Data schemas for the book_statuses service."""
from marshmallow import fields, Schema, EXCLUDE


class BookStatusesSchema(Schema):
    """Base data schema for a book status."""
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    display_name = fields.String(required=True)
    order_index = fields.Integer(required=True)

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE
