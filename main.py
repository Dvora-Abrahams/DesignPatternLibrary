# main.py

from common.book import Book
from common.user import User
from common.book_category import BookCategory
from decorator.rare_book_decorator import RareBookDecorator
from decorator.library_only_decorator import LibraryOnlyDecorator
from bridge.text_color_display import TextColorDisplay
from bridge.background_color_display import BackgroundColorDisplay
from adapter.red import Red
from adapter.adapter_library import Adapter
from facade.library_facade import LibraryFacade
from flyweight.book_factory import BookFactory
from composite.books_in_category import BooksInCategory
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# יצירת משתמשים
regular_user = User("moshe", is_premium=False)
premium_user = User("esti", is_premium=True)

# יצירת Adapter לכל קטגוריה
young_adult_adapter = Adapter(TextColorDisplay())
holocaust_adapter = Adapter(TextColorDisplay())
children_adapter = Adapter(BackgroundColorDisplay())
adult_adapter = Adapter(TextColorDisplay())

# יצירת קטגוריות עם Adapter + Bridge
young_adult = BooksInCategory(BookCategory.YOUNG_ADULT, adapter=young_adult_adapter)
holocaust = BooksInCategory(BookCategory.HOLOCAUST, adapter=holocaust_adapter)
children = BooksInCategory(BookCategory.CHILDRENS_BOOKS, adapter=children_adapter)

# קטגוריית אב
adult = BooksInCategory(BookCategory.ADULT, [young_adult, holocaust, children], adapter=adult_adapter)

# יצירת ספרים עם Flyweight ו־Decorator
thriller_book = BookFactory.get_book(Book("the book", "Avigail", BookCategory.YOUNG_ADULT))
rare_book = BookFactory.get_book(RareBookDecorator(Book("Codex Leicester", "Leonardo da Vinci", BookCategory.YOUNG_ADULT)))
adult_book = BookFactory.get_book(Book("The glass", "Shoshana", BookCategory.ADULT))
children_book = BookFactory.get_book(Book("chocolate factory", "David", BookCategory.CHILDRENS_BOOKS))
library_only = BookFactory.get_book(LibraryOnlyDecorator(Book("Old book", "dont know", BookCategory.ADULT)))

# יצירת ספרייה (Facade)
library = LibraryFacade(adult)

# הוספת ספרים
library.add_book(thriller_book)
library.add_book(rare_book)
library.add_book(adult_book)
library.add_book(children_book)
library.add_book(library_only)

print("\n" + "*" * 40 + "\n")

# השאלת ספרים
print(f"{regular_user.name} borrowing thriller book:", library.borrow_book("the book", regular_user))
print(f"{regular_user.name} borrowing rare book:", library.borrow_book("Codex Leicester", regular_user))
print(f"{premium_user.name} borrowing rare book:", library.borrow_book("Codex Leicester", premium_user))
print(f"{premium_user.name} borrowing thriller book:", library.borrow_book("the book", premium_user))
print(f"{premium_user.name} borrowing 'The glass':", library.borrow_book("The glass", premium_user))
print(f"{premium_user.name} borrowing 'chocolate factory':", library.borrow_book("chocolate factory", premium_user))
print(f"{regular_user.name} borrowing library only book:", library.borrow_book("Old book", regular_user))

print("\n" + "*" * 40 + "\n")

# החזרת ספרים
print("Regular user returned thriller book:", library.return_book("the book" , regular_user))
print("Regular user returned rare book:", library.return_book("Codex Leicester" , regular_user))
print("Premium user returned thriller book:", library.return_book("the book" , premium_user))
print("Premium user returned 'The glass':", library.return_book("The glass" , premium_user))
print("Premium user returned 'chocolate factory':", library.return_book("chocolate factory" , premium_user))

