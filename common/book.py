from datetime import datetime
from common.ibook import IBook
from common.book_category import BookCategory

class Book(IBook):
    _id_counter = 0

    def __init__(self, name="", author="", category=None):
        Book._id_counter += 1
        self._id = Book._id_counter
        self._name = name
        self._author = author
        self._category = category
        self.is_borrowed = False
        self._borrowing_date = None
        self.borrowed_by = None


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def category(self):
        return self._category

    def borrow(self, user):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        self._borrowing_date = datetime.now()
        self.borrowed_by = user
        return True

    def return_book(self, user=None):
        if not self.is_borrowed:
            return False
        if user and user != self.borrowed_by:
            print(f"⚠️ {user.name} didn't borrow this book.")
            return False
            self.is_borrowed = False
        self.borrowed_by = None
        return True


    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Author: {self.author}\n"
            f"Id: {self.id}\n"
            f"Is Borrowed: {self.is_borrowed}\n"
            f"Borrowing Date: {self._borrowing_date}\n"
        )
