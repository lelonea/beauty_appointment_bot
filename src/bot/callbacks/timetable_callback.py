import logging

from aiogram import types

from bot.handlers.keyboards import CalendarKeyboards
from core.api.callback_handler import BaseCallbackHandler
from db.schemas.callbacks import CallbackData

logger = logging.getLogger(__name__)


class TimeTableOptionsCallbackHandler(BaseCallbackHandler):
    @staticmethod
    async def _choose_date(callback_query: types.CallbackQuery) -> None:
        calendar_keyboard = await CalendarKeyboards.get_simple_calendar()
        await callback_query.message.edit_text("Выберите дату",
                                               reply_markup=calendar_keyboard)

    async def run(self, callback_query: types.CallbackQuery) -> None:
        logger.info("TimeTableOptionsCallbackHandler started")
        logger.info(f"Callback query {callback_query.data} from user {callback_query.from_user.id}")
        data = CallbackData.parse_raw(callback_query.data)

        logger.info(f"ACTION: {data.action}")

        if data.action == "add":
            await self._choose_date(callback_query)
