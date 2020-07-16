from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    @abstractmethod
    def get_range(self) -> str:
        pass

    @abstractmethod
    def format(self) -> str:
        pass
