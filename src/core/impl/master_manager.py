import logging

from aiogram.types import User as TgUser

from core.api.base_master_manager import BaseMasterManager
from db import get_db
from db.db_client import DBClient

logger = logging.getLogger(__name__)


class MasterManager(BaseMasterManager):
    def __init__(self):
        self._db_client: DBClient = get_db()

    async def register_user(self, tg_user: TgUser):
        logger.info(f"Registering user in db {tg_user.id}")
        user = await self._db_client.create_master_user(tg_user)
        return user
