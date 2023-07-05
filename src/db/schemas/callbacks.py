from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CallbackDataType(Enum):
    register = 1
    timetable_options = 2


class CallbackData(BaseModel):
    class Config:
        orm_mode = True

    type: CallbackDataType
    action: Optional[str] = None
