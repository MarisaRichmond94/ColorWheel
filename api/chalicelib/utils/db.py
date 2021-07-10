"""Utility file for reusable database functionality."""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import db

engine = create_engine(db.DATABASE_URI)
Session = sessionmaker(bind=engine)
SESSION = None


@contextmanager
def session_scope():
    """Context manager for a database session."""
    session = Session()

    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
