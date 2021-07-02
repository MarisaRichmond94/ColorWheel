"""Helper function for populating the genres on a user book."""
from restful_services.book_genres import business as book_genres_service


def populate_genres_for_user_book(session: any, user_book: dict) -> dict:
    """Populates the primary and secondary genres for a user's book.

    Args:
        session: The current database session for the request.
        user_book: The book to populate genres onto.

    Returns:
        The given user_book with its primary and secondary genres populated.
    """
    user_book_genres = book_genres_service.get_book_genres_by_book_id(
        session,
        book_id=user_book.get('id')
    )
    user_book['primary_genre'] = next((
        user_book_genre
        for user_book_genre in user_book_genres
        if user_book_genre.get('is_primary')
    ), None)
    user_book['secondary_genres'] = [
        user_book_genre
        for user_book_genre in user_book_genres
        if not user_book_genre.get('is_primary')
    ]

    return user_book
