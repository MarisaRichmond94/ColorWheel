from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func

from db_models.base_model import Base
from db_models.dim_users import DimUsers


@DimUsers.dimension
class FctSessions(Base):
    __tablename__ = "fct_sessions"
    token = Column(String, unique=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
