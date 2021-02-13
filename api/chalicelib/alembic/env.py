# pylint: disable=wrong-import-position, unused-import
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

parent_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(parent_dir)
sys.path.insert(0, os.path.abspath("chalicelib"))

from db_models.base_model import Base, BaseModel
from db_models.dim_users import DimUsers
from db_models.fct_sessions import FctSessions

from settings import db


config = context.config

fileConfig(config.config_file_name)

target_metadata = [
    Base.metadata,
    BaseModel.metadata,
]

def run_migrations_offline():
    context.configure(
        url=db.DATABASE_URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(db.DATABASE_URI)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table="alembic_version",
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
