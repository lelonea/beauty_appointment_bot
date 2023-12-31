import logging
import os
from enum import Enum
from urllib.parse import urljoin


class BotMode(Enum):
    polling = "polling"
    webhooks = "webhooks"


BOT_MODE = BotMode(os.getenv("BOT_MODE", BotMode.polling.value).lower())

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

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
