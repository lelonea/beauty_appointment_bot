import logging

from aiogram import types
from bot.constants import START_MESSAGE


logger = logging.getLogger(__name__)


async def send_welcome(message: types.Message) -> None:
    logger.info(f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} started bot")
    await message.answer(START_MESSAGE, parse_mode=types.ParseMode.MARKDOWN)