"""The database model for the fct_books table."""
from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db_models.base_model import Base
from db_models.dim_book_statuses import DimBookStatuses
from db_models.dim_users import DimUsers
from settings.db import MAX_STRING_LENGTH


@DimBookStatuses.dimension
@DimUsers.dimension
class FctBooks(Base):
    """SQLAlchemy object for the fct_books table."""
    __tablename__ = 'fct_books'
    author = Column(String(MAX_STRING_LENGTH), nullable=False)
    image_key = Column(String(MAX_STRING_LENGTH), nullable=True)
    synopsis = Column(String(MAX_STRING_LENGTH), nullable=True)
    timestamp = Column(DateTime(), nullable=False)
    title = Column(String(MAX_STRING_LENGTH), nullable=False)

    @classmethod
    def dimension(cls, target):
        """Class for creating a relationship to the fct_books table."""
        target.fct_book_id = Column(
            'fct_book_id',
            UUID(as_uuid=True),
            ForeignKey(FctBooks.id),
            nullable=False,
        )
        target.fct_book = relationship(cls, lazy='subquery')
        return target
