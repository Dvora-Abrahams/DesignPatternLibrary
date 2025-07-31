from composite.books_in_category import BooksInCategory
from flyweight.book_factory import BookFactory
from common.ibook import IBook
from common.user import User

class LibraryFacade:
    def __init__(self, root_category: BooksInCategory):
        self.root_category = root_category

    def add_book(self, book: IBook) -> bool:
        # מקבל ספר, מביא אותו מה־factory (כדי להשתמש בגרסה משותפת אם יש)
        flyweight_book = BookFactory.get_book(book)
        return self.root_category.add(flyweight_book)

    def find_book(self, title: str) -> IBook | None:
        return self.root_category.find_by_name(title)

    def borrow_book(self, title: str, user: User) -> bool:
        book = self.find_book(title)
        if book is None:
            print("❌ The book is not found.")
            return False

        if not book.borrow(user):
            print("⚠️ Book could not be borrowed.")
            return False

        print("✅ Book borrowed successfully.")
        return True

    # בקובץ: library_facade.py
    def return_book(self, title: str, user) -> bool:
        book = self.find_book(title)
        if book is None:
            print("❌ The book is not found.")
            return False
        result = book.return_book(user)
        if result:
            print("✅ Book returned successfully.")
        else:
            print("⚠️ Book was not returned.")
        return result
