from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from bot.handlers.callback_handlers import CallbackHandlerPipeline
from bot.handlers.command_handlers import send_welcome, send_help

from settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Commands
dp.register_message_handler(send_welcome, commands=["start"])
dp.register_message_handler(send_help, commands=["help"])

dp.register_callback_query_handler(CallbackHandlerPipeline())
