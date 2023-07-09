from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_calendar import SimpleCalendar

from core.schemas.callbacks import CallbackData, CallbackDataType


class Keyboards:
    @staticmethod
    def get_start_button():
        callback_data = CallbackData(type=CallbackDataType.register)
        start_button = InlineKeyboardButton("Старт", callback_data=callback_data.json(indent=None))
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(start_button)
        return keyboard

    @staticmethod
    def get_timetable_options():
        callback_data_add = CallbackData(type=CallbackDataType.timetable_options, action="add")
        callback_data_remove = CallbackData(type=CallbackDataType.timetable_options, action="remove")
        callback_data_get = CallbackData(type=CallbackDataType.timetable_options, action="get")
        add_slot = InlineKeyboardButton("Добавить окошки для записи", callback_data=callback_data_add.json(indent=None))
        remove_slot = InlineKeyboardButton("Удалить окошки для записи", callback_data=callback_data_remove.json(indent=None))
        get_timetable = InlineKeyboardButton("Получить расписание", callback_data=callback_data_get.json(indent=None))
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(add_slot, remove_slot, get_timetable)
        return keyboard


class CalendarKeyboards:
    simple = SimpleCalendar()

    @classmethod
    async def get_simple_calendar(cls):
        return await cls.simple.start_calendar()


