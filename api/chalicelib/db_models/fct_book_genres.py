"""The database model for the fct_book_genres table."""
from db_models.base_model import Base
from db_models.fct_books import FctBooks
from db_models.fct_genres import FctGenres


@FctBooks.dimension
@FctGenres.dimension
class FctBookGenres(Base):
    """SQLAlchemy object for the fct_book_genres table."""
    __tablename__ = 'fct_book_genres'
