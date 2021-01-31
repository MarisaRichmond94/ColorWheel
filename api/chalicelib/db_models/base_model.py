"""Base model to be used across every DB model"""
from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base, as_declarative

BaseModel = declarative_base()


@as_declarative()
class Base:
    """SQLAlchemy declarative base that gives you a column called id (primary key)"""

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")
    )