"""Data schemas for the genres service."""
from marshmallow import fields, Schema, EXCLUDE


class GenresSchema(Schema):
    """Base data schema for a genre."""
    id = fields.UUID(required=True)
    # add any attributes

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE


class PopulatedGenresSchema(Schema):
    """Populated data schema for a genre."""
    id = fields.UUID(required=True)
    # add any attributes

    class Meta:
        """Meta class."""
        ordered = True
        unknown = EXCLUDE
