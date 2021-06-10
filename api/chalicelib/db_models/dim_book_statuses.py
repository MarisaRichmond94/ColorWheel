"""The database model for the dim_book_statuses table."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db_models.base_model import Base
from settings.db import DB_STRING_MAX_LENGTH


class DimBookStatuses(Base):
    """SQLAlchemy object for the dim_book_statuses table."""
    __tablename__ = 'dim_book_statuses'
    name = Column(String(DB_STRING_MAX_LENGTH), nullable=False)
    display_name = Column(String(DB_STRING_MAX_LENGTH), nullable=False)
    order_index = Column(Integer(), nullable=False)

    @classmethod
    def dimension(cls, target):
        """Class for creating a relationship to the dim_book_statuses table."""
        target.dim_book_status_id = Column(
            'dim_book_status_id',
            UUID(as_uuid=True),
            ForeignKey(DimBookStatuses.id),
            nullable=False,
        )
        target.dim_book_status = relationship(cls)
        return target
