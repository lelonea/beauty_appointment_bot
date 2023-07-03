from aiogram import types

from bot.callbacks.register_callbacks import RegisterCallbackHandler
from bot.callbacks.timetable_callback import TimeTableOptionsCallbackHandler
from db.schemas.callbacks import CallbackDataType, CallbackData


class CallbackHandlerPipeline:
    def __init__(self):
        self._callback_handlers = {
            CallbackDataType.register: RegisterCallbackHandler(),
            CallbackDataType.timetable_options: TimeTableOptionsCallbackHandler(),
        }

    async def __call__(self, callback_query: types.CallbackQuery) -> None:
        data = CallbackData.parse_raw(callback_query.data)
        handler = self._callback_handlers[data.type]
        try:
            await handler.run(callback_query)
        except Exception as exc:
            print(exc)
