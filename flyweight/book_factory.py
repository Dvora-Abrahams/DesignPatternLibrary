from typing import Dict, List
from common.ibook import IBook
from common.book import Book

class BookFactory:
    _books_cache: Dict[str, IBook] = {}

    @classmethod
    def get_book(cls, book: IBook) -> IBook:
        key = f"{book.name}-{book.author}-{book.category.name}"

        if key not in cls._books_cache:
            cls._books_cache[key] = Book(book.name, book.author, book.category)

        base_book = cls._books_cache[key]

        # אם הספר הוא דקורטור – נעטוף את הספר הבסיסי בדקורטור מהסוג של הספר המקורי
        if hasattr(book, "__class__") and isinstance(book, IBook) and type(book) != Book:
            return type(book)(base_book)

        return base_book

    @classmethod
    def get_all_books(cls) -> List[IBook]:
        return list(cls._books_cache.values())
