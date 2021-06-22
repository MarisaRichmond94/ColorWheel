"""Settings file for restful_services-related settings."""
from utils.alembic.fixtures.book_statuses import book_statuses_fixture


INITIAL_BOOK_STATUS_ID = book_statuses_fixture[0].get('id')
