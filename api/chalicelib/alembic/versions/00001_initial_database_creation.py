"""Initial Database Creation

Revision ID: 000000000001
Revises: None
Create Date: 2021-02-28 21:59:44.964998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker

# Table Fixture Imports
from utils.alembic.fixtures.book_statuses import book_statuses_fixture
from utils.alembic.fixtures.genres import genres_fixture
from utils.alembic.fixtures.users import users_fixture

# revision identifiers, used by Alembic.
revision = '000000000001'
down_revision = None
branch_labels = None
depends_on = None


Session = sessionmaker()
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute('create extension if not exists "uuid-ossp";')

    ### DIM BOOK STATUSES ###
    book_statuses_table = op.create_table(
        'dim_book_statuses',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('name', sa.String(length=2048), nullable=False),
        sa.Column('display_name', sa.String(length=2048), nullable=False),
        sa.Column('order_index', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(book_statuses_table, book_statuses_fixture)

    ### DIM USERS ###
    users_table = op.create_table(
        'dim_users',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('name', sa.String(length=2048), nullable=False),
        sa.Column('email', sa.String(length=2048), nullable=False),
        sa.Column('password', sa.LargeBinary(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.bulk_insert(users_table, users_fixture)

    ### FCT BOOKS ###
    op.create_table(
        'fct_books',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('author', sa.String(length=2048), nullable=False),
        sa.Column('image_key', sa.String(length=2048), nullable=True),
        sa.Column('summary', sa.String(length=2048), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('title', sa.String(length=2048), nullable=False),
        sa.Column('dim_user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('dim_book_status_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['dim_book_status_id'], ['dim_book_statuses.id'], ),
        sa.ForeignKeyConstraint(['dim_user_id'], ['dim_users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    ### FCT GENRES ###
    genres_table = op.create_table(
        'fct_genres',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('bucket_name', sa.String(length=2048), nullable=True),
        sa.Column('display_name', sa.String(length=2048), nullable=False),
        sa.Column('is_primary', sa.Boolean(), nullable=False),
        sa.Column('name', sa.String(length=2048), nullable=False),
        sa.Column('dim_user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['dim_user_id'], ['dim_users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(genres_table, genres_fixture)

    ### FCT BOOK GENRES ###
    op.create_table(
        'fct_book_genres',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('fct_genre_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('fct_book_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['fct_book_id'], ['fct_books.id'], ),
        sa.ForeignKeyConstraint(['fct_genre_id'], ['fct_genres.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    ### FCT SESSIONS ###
    op.create_table(
        'fct_sessions',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column(
            'timestamp',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True
        ),
        sa.Column('dim_user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(['dim_user_id'], ['dim_users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fct_sessions')
    op.drop_table('fct_book_genres')
    op.drop_table('fct_genres')
    op.drop_table('fct_books')
    op.drop_table('dim_users')
    op.drop_table('dim_book_statuses')
    # ### end Alembic commands ###
