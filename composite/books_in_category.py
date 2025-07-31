from typing import List, Optional
from common.ibook import IBook
from common.book_category import BookCategory

class BooksInCategory:

    def __init__(self, category: BookCategory, subcategories: Optional[List["BooksInCategory"]] = None, adapter=None):
        self.category = category
        self.subcategories = subcategories if subcategories is not None else []
        self.books: List[IBook] = []
        self.adapter = adapter

    def add(self, book: IBook) -> bool:
        if book.category == self.category:
            self.books.append(book)
            print(f"✅ Book '{book.name}' added to category {self.category.name}")
            return True

        for sub in self.subcategories:
            if sub.add(book):
                return True

        print(f"⚠️ Book '{book.name}' could not be added – no matching category found.")
        return False

    def find_by_name(self, title: str) -> Optional[IBook]:
        for book in self.books:
            if book.name == title:
                if self.adapter:
                    self.adapter.category = self.category
                    self.adapter.print(str(book))
                else:
                    print(f"📚 Book found: {book.name} in category {self.category.name}")
                ##print(f"📚 Book found: {book}")
                return book

        for sub in self.subcategories:
            result = sub.find_by_name(title)
            if result is not None:
                return result

        print(f"❌ Book '{title}' not found.")
        return None
