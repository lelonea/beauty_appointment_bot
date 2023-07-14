import asyncio
import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
sys.path = ['', '..'] + sys.path[1:]

try:
    from db.models import Base
    target_metadata = Base.metadata
except Exception as e:
    target_metadata = None
    print(e)
    print("CUSTOM METADATA IS IGNORED")


def get_connection_string():
    db_username = os.environ.get("MARIADB_USER")
    db_password = os.environ.get("MARIADB_PASSWORD")
    db_endpoint = os.environ.get("DB_ENDPOINT")
    db_port = os.environ.get("DB_PORT", "3306")
    db_name = os.getenv("MARIADB_DATABASE")
    section = config.get_section(config.config_ini_section)
    url = section["sqlalchemy.url"].format(db_username, db_password, db_endpoint, db_port, db_name)
    print(url)
    return url

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_connection_string()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, compare_type=True, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context .

    """
    alembic_config = config.get_section(config.config_ini_section)
    alembic_config["sqlalchemy.url"] = get_connection_string()

    connectable = AsyncEngine(
        engine_from_config(
            alembic_config,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
