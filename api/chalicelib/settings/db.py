"""Settings file for constants related to the database."""
import os


MAX_STRING_LENGTH = int(os.getenv('MAX_STRING_LENGTH', '2048'))
POSTGRES_DB = os.getenv('POSTGRES_DB', 'colorwheel')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', '5432'))
POSTGRES_USER = os.getenv('POSTGRES_USER', 'user')


DATABASE_URI = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)
DATABASE_URI_MASKED = (
    f'postgresql://{POSTGRES_USER}:***'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)
