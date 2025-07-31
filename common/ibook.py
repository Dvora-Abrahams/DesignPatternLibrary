from abc import ABC, abstractmethod

class IBook(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @property
    @abstractmethod
    def category(self): pass

    @property
    @abstractmethod
    def id(self): pass

    @property
    @abstractmethod
    def author(self): pass

    @abstractmethod
    def borrow(self, user): pass

    @abstractmethod
    def return_book(self): pass
