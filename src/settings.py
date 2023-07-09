import logging
import os
from urllib.parse import urljoin

from core.schemas.common import BotMode, BotType


logging.basicConfig(level=logging.INFO)

# bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_MODE = BotMode(os.getenv("BOT_MODE", BotMode.polling.value).lower())
BOT_TYPE = BotType(os.getenv("BOT_TYPE", BotType.master.value).lower())
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "ru")
LOCALE_PATHS = os.path.join(os.path.dirname(__file__), "locales", BOT_TYPE.value)


# webhook settings
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_PATH)

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", "80"))

# database settings
MARIADB_USER = os.getenv("MARIADB_USER")
MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")
DB_ENDPOINT = os.getenv("DB_ENDPOINT")
DB_PORT = os.getenv("DB_PORT")
MARIADB_DATABASE = os.getenv("MARIADB_DATABASE")
DATABASE_CONNECTION_STRING = f"mariadb+asyncmy://{MARIADB_USER}:{MARIADB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{MARIADB_DATABASE}"
