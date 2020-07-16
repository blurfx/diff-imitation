from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    @abstractmethod
    def get_range(self) -> str:
        """
        get changed range of document as ed style format (e.g. "11,15d16", "0a1,6")

        :return: colored changed range of document
        """
        pass

    @abstractmethod
    def format(self) -> str:
        """
        get colored and formatted diff output string (separated by '\n')
        :return: colored and formatted diff output
        """
        pass
