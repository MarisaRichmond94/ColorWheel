"""Initial database setup

Revision ID: 000000000001
Revises: None
Create Date: 2021-01-31 04:39:59.933950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '000000000001'
down_revision = None
branch_labels = None
depends_on = None


Session = sessionmaker()
def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute('create extension if not exists "uuid-ossp";')
    op.create_table(
        'dim_users',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False
        ),
        sa.Column('name', sa.String(length=2048), nullable=False),
        sa.Column('email', sa.String(length=2048), unique=True, nullable=False),
        sa.Column('password', sa.String(length=2048), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('dim_users')
