import logging

from aiogram import types

from core.api.callback_handler import BaseCallbackHandler
from utils.exceptions import DuplicationException

logger = logging.getLogger(__name__)


class RegisterCallbackHandler(BaseCallbackHandler):
    async def run(self, callback_query: types.CallbackQuery) -> None:
        try:
            logger.info(f"Registering user {callback_query.from_user.id}")
            await self._master_manager.register_user(callback_query.from_user)
            await callback_query.message.edit_text(
                "Вы успешно зарегистрированы!",
                parse_mode=types.ParseMode.MARKDOWN,
            )
        except DuplicationException:
            await callback_query.message.edit_text(
                "Вы уже зарегистрированы!",
                parse_mode=types.ParseMode.MARKDOWN,
            )
