from abc import ABC, abstractmethod

class IColor(ABC):
    @abstractmethod
    def color_console(self) -> str:
        """Return a color name (e.g. 'red', 'blue') as string"""
        pass
