from abc import ABC, abstractmethod
from typing import List

from diff import DiffResult


class BaseFormatter(ABC):
    @abstractmethod
    def __init__(self, items: List[DiffResult]):
        pass

    @abstractmethod
    def get_range(self) -> str:
        pass

    @abstractmethod
    def format(self) -> str:
        pass
