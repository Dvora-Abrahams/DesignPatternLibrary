from .book_decorator import BookDecorator
from common.ibook import IBook

class RareBookDecorator(BookDecorator):
    def __init__(self, book: IBook):
        super().__init__(book)

    def borrow(self, user):
        if not getattr(user, "is_premium", False):
            print(f"❌ {user.name}, You are not a premium user! A rare book can only be borrowed by premium users..")
            return False
        return self.book.borrow(user)

    def return_book(self, user):
        return self.book.return_book(user)
