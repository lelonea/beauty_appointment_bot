from abc import ABC, abstractmethod


class BaseLocalization(ABC):
    @abstractmethod
    def get(self, key: str, language: str = None) -> str:
        pass
