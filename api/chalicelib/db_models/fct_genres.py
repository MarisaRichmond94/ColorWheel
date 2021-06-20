"""The database model for the fct_genres table."""
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db_models.base_model import Base
from db_models.dim_users import DimUsers
from settings.db import MAX_STRING_LENGTH


@DimUsers.dimension
class FctGenres(Base):
    """SQLAlchemy object for the fct_genres table."""
    __tablename__ = 'fct_genres'
    bucket_name = Column(String(MAX_STRING_LENGTH), nullable=True)
    display_name = Column(String(MAX_STRING_LENGTH), nullable=False)
    is_primary = Column(Boolean(), nullable=False)
    name = Column(String(MAX_STRING_LENGTH), nullable=False)

    @classmethod
    def dimension(cls, target):
        """Class for creating a relationship to the fct_genres table."""
        target.fct_genre_id = Column(
            'fct_genre_id',
            UUID(as_uuid=True),
            ForeignKey(FctGenres.id),
            nullable=False,
        )
        target.fct_genre = relationship(cls, lazy='subquery')
        return target
