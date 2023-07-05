import logging

from aiogram.types import User as TgUser
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker

from db.db_client import DBClient
import settings
from db.models import Base, Master
from utils.exceptions import DuplicationException, ForeignKeyException

logger = logging.getLogger(__name__)


class MariaDBClient(DBClient):
    __instance = None
    engine = None
    session = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        super(MariaDBClient, self).__init__(*args, **kwargs)
        if self.engine is None:
            logging.info("Connecting to MariaDB")

            self.engine: AsyncEngine = create_async_engine(
                settings.DATABASE_CONNECTION_STRING,
                pool_pre_ping=True,
                pool_size=5,
                max_overflow=0,
                pool_recycle=3600,
            )
            self.session: async_sessionmaker = async_sessionmaker(bind=self.engine, expire_on_commit=False)

            logging.info("MariaDB connected")

    async def _insert(self, row: Base):
        try:
            async with self.session() as session:
                logger.info(f"Inserting row {row}")
                session.add(row)
                await session.flush()
                row_id = row.id
                logger.info(f"Row {row_id} before commit")
                await session.commit()
                logger.info(f"Row {row_id} inserted")
                return row_id
        except IntegrityError as e:
            if "Duplicate entry" in e.orig.args[1]:
                raise DuplicationException(e.orig.args[1])
            elif "Cannot add or update a child row: a foreign key constraint fails" in e.orig.args[1]:
                raise ForeignKeyException(e.orig.args[1])
            raise e

    async def create_master_user(self, tg_user: TgUser) -> Master:
        logger.info(f"Making query to create user {tg_user.id}")
        user = Master(id=tg_user.id, username=tg_user.username, full_name=tg_user.full_name)
        logger.info(f"Inserting user {tg_user.id}")
        return await self._insert(user)
