"""Base database model."""
from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base, as_declarative

BaseModel = declarative_base()


@as_declarative()
class Base:
    """The base declarative model for a database table model."""
    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')
    )
