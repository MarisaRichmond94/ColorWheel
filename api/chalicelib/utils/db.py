"""utils for db functionality"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import db

engine = create_engine(db.DATABASE_URI)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Context manager to handle database sessions."""
    session = Session()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
