from abc import ABC

from core.api.base_master_manager import BaseMasterManager
from core.impl.master_manager import MasterManager
from db import get_db
from db.db_client import DBClient


class BaseCallbackHandler(ABC):
    def __init__(self):
        self._db_client: DBClient = get_db()
        self._master_manager: BaseMasterManager = MasterManager()


