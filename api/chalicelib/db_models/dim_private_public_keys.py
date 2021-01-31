"""DB Model for dim_private_public_keys"""
from sqlalchemy import Column, String

from db_models.base_model import Base
from settings.db import DB_STRING_MAX_LENGTH


class DimPrivatePublicKeys(Base):
    """SQLAlchemy object for dim_private_public_keys"""
    __tablename__ = "dim_private_public_keys"
    private_pem_object_key = Column(String(DB_STRING_MAX_LENGTH), unique=True, nullable=False)
    public_pem_object_key = Column(String(DB_STRING_MAX_LENGTH), unique=True, nullable=False)
