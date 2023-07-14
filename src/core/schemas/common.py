from enum import Enum


class BotMode(Enum):
    polling = "polling"
    webhooks = "webhooks"


class BotType(Enum):
    master = "master"
    client = "client"
