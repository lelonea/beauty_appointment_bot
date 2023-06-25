from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from .handlers.command_handlers import send_welcome

from settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Commands
dp.register_message_handler(send_welcome, commands=["start", "help"])
