from sqlalchemy import Column, LargeBinary, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db_models.base_model import Base
from settings.db import DB_STRING_MAX_LENGTH


class DimUsers(Base):
    __tablename__ = "dim_users"
    name = Column(String(DB_STRING_MAX_LENGTH), nullable=False)
    email = Column(String(DB_STRING_MAX_LENGTH), unique=True, nullable=False)
    password = Column(LargeBinary(), nullable=False)

    @classmethod
    def dimension(cls, target):
        target.dim_user_id = Column(
            "dim_user_id",
            UUID(as_uuid=True),
            ForeignKey(DimUsers.id),
            nullable=False,
        )
        target.dim_user = relationship(cls)
        return target
