from abc import ABC, abstractmethod

class ColorDisplay(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def color(self, color):
        pass

    @abstractmethod
    def reset(self):
        pass
