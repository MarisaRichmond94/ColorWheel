"""API schemas for the books service."""
from marshmallow import fields, Schema


class CreateBookBodySchema(Schema):
    """Schema for creating a new book."""
    id = fields.UUID(required=False)
    author = fields.String(required=True)
    image_key = fields.String(required=False)
    summary = fields.String(required=False)
    title = fields.String(required=True)


class GetBooksQuerySchema(Schema):
    """Schema for getting books."""
    user_id = fields.UUID(required=False)


class UpdateBookBodySchema(Schema):
    """Schema for updating a book."""
    title = fields.String(required=False)
    author = fields.String(required=False)
    summary = fields.String(required=False)
    image_key = fields.String(required=False)
    book_status_id = fields.UUID(required=False)


class DeleteBooksQuerySchema(Schema):
    """Schema for deleting books."""
    user_id = fields.UUID(required=True)
