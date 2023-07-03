from db.adapters.mariadb_adapter import MariaDBClient
from db.db_client import DBClient


def get_db() -> DBClient:
    return MariaDBClient()
