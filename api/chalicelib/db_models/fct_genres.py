"""The database model for the fct_genres table."""
from sqlalchemy import Boolean, Column, String

from db_models.base_model import Base
from db_models.dim_users import DimUsers
from settings.db import DB_STRING_MAX_LENGTH


@DimUsers.dimension
class FctGenres(Base):
    """SQLAlchemy object for the fct_genres table."""
    __tablename__ = 'fct_genres'
    name = Column(String(DB_STRING_MAX_LENGTH), unique=True, nullable=False)
    display_name = Column(String(DB_STRING_MAX_LENGTH), unique=True, nullable=False)
    bucket_name = Column(String(DB_STRING_MAX_LENGTH), nullable=True)
    is_primary = Column(Boolean, nullable=False)
