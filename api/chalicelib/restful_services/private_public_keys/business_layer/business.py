"""Business layer for the private public keys service"""
from typing import Dict, Optional

from utils.validation import validate_params
from restful_services.private_public_keys.data_layer import data


def get_private_public_key() -> Optional[Dict]:
    """Gets all private public keys from the dim_private_public_keys table

    Returns:
        JSON representation of a prive public key (there should only ever be one)
    """
    return data.get_private_public_key()
