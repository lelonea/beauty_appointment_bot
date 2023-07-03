from enum import Enum

from pydantic import BaseModel


class CallbackDataType(Enum):
    register = 1


class CallbackData(BaseModel):
    class Config:
        orm_mode = True

    type: CallbackDataType
