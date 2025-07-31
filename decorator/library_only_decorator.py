from .book_decorator import BookDecorator
from common.ibook import IBook

class LibraryOnlyDecorator(BookDecorator):
    def __init__(self, book: IBook):
        super().__init__(book)

    def borrow(self, user):
        print("The book is intended for reading in the library only!")
        return False

    def return_book(self):
        print("The book is intended for reading in the library only!")
        return False
