from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db.schemas.callbacks import CallbackData, CallbackDataType


class Keyboards:
    @staticmethod
    def get_start_button():
        callback_data = CallbackData(type=CallbackDataType.register)
        start_button = InlineKeyboardButton("Старт", callback_data=callback_data.json(indent=None))
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(start_button)
        return keyboard
