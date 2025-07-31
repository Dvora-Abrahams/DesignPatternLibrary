from common.ibook import IBook


class BookDecorator(IBook):
    def __init__(self, book: IBook):
        self.book = book

    @property
    def name(self):
        return self.book.name

    @name.setter
    def name(self, value):
        self.book.name = value

    @property
    def category(self):
        return self.book.category

    @category.setter
    def category(self, value):
        self.book.category = value

    @property
    def id(self):
        return self.book.id

    @id.setter
    def id(self, value):
        self.book.id = value

    @property
    def author(self):
        return self.book.author

    @author.setter
    def author(self, value):
        self.book.author = value

    def borrow(self, user):
        return self.book.borrow(user)

    def return_book(self):
        return self.book.return_book()