from abc import ABC, abstractmethod


class DBClient(ABC):
    @abstractmethod
    async def create_master_user(self, tg_user) -> None:
        pass
