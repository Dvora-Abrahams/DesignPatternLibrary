from enum import Enum

class BookCategory(Enum):
    NA = 0
    THRILLER = 1
    BIOGRAPHY = 2
    SELF_HELP = 4
    HISTORY = 8
    HOLOCAUST = 16
    YOUNG_ADULT = 32
    CHILDRENS_BOOKS = 64
    ADULT = 128
    FANTASY = 256