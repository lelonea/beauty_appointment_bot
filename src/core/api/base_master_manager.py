from abc import ABC, abstractmethod


class BaseMasterManager(ABC):
    @abstractmethod
    async def register_user(self, user) -> None:
        pass
