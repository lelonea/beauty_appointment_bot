from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from bot.handlers.callback_handlers import CallbackHandlerPipeline
from bot.handlers.command_handlers import send_welcome, send_help, send_timetable_options
from core.schemas.common import BotType

from settings import BOT_TOKEN, BOT_TYPE


def set_up_master_dispatcher(dispatcher: Dispatcher) -> None:
    # Commands
    dp.register_message_handler(send_welcome, commands=["start"])
    dp.register_message_handler(send_help, commands=["help"])
    dp.register_message_handler(send_timetable_options, commands=["timetable"])

    # Callbacks
    dp.register_callback_query_handler(CallbackHandlerPipeline())


def set_up_client_dispatcher(dispatcher: Dispatcher) -> None:
    pass


DISPATCHERS = {
    BotType.master: set_up_master_dispatcher,
    BotType.client: set_up_client_dispatcher,
}

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

DISPATCHERS[BOT_TYPE](dp)
