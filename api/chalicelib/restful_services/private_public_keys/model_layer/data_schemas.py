"""Data schemas for the private public keys service"""
from marshmallow import fields, Schema, EXCLUDE

class PrivatePublicKeySchema(Schema):
    """Data schema for a private public key"""
    id = fields.UUID(required=True)
    private_pem_object_key = fields.String(required=True)
    public_pem_object_key = fields.String(required=True)

    class Meta:
        """Meta class for private public keys schema"""
        unknown = EXCLUDE
