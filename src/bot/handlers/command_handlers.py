import logging

from aiogram import types
from bot.handlers.keyboards import Keyboards
from core.impl.localization import Localization

logger = logging.getLogger(__name__)

keyboards = Keyboards()
locale = Localization()


async def send_welcome(message: types.Message) -> None:
    logger.info(f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} started bot")
    await message.answer(locale.get("START_MESSAGE"), parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboards.get_start_button())


async def send_help(message: types.Message) -> None:
    logger.info(
        f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} asked for help")
    await message.answer(locale.get("HELP_MESSAGE"), parse_mode=types.ParseMode.MARKDOWN)


async def send_timetable_options(message: types.Message) -> None:
    logger.info(
        f"User {message.from_user.id} {message.from_user.username} {message.from_user.full_name} asked for timetable options")
    await message.answer("Выберите действие", reply_markup=keyboards.get_timetable_options())
