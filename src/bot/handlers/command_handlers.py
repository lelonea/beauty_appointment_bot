import logging

from aiogram import types
from bot.constants import START_MESSAGE, HELP_MESSAGE
from bot.handlers.keyboards import Keyboards

logger = logging.getLogger(__name__)

keyboards = Keyboards()


async def send_welcome(message: types.Message) -> None:
    logger.info(f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} started bot")
    await message.answer(START_MESSAGE, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboards.get_start_button())


async def send_help(message: types.Message) -> None:
    logger.info(
        f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} asked for help")
    await message.answer(HELP_MESSAGE, parse_mode=types.ParseMode.MARKDOWN)
