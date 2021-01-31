"""Data layer for the private public keys service"""
from typing import Dict, Optional

from db_models.dim_private_public_keys import DimPrivatePublicKeys
from utils import db
from restful_services.private_public_keys.model_layer.data_schemas import PrivatePublicKeySchema


def get_private_public_key() -> Optional[Dict]:
    """Gets all private public keys from the dim_private_public_keys table

    Returns:
        JSON representation of a prive public key (there should only ever be one)
    """
    with db.session_scope() as session:
        private_public_keys = session.query(DimPrivatePublicKeys).all()
        return PrivatePublicKeySchema(many=True).dump(user)[0] if private_public_keys else None
