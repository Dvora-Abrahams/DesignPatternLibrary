from bridge.color_display import ColorDisplay
from common.book_category import BookCategory
from adapter.red import Red
from adapter.blue import Blue
from adapter.yellow import Yellow
class Adapter:
    def __init__(self, color_display: ColorDisplay):
        self.color_display = color_display

    def print(self, text=""):
        if self.color_display:
            if self.category == BookCategory.ADULT:
                self.color_display.color(Blue())
            elif self.category == BookCategory.YOUNG_ADULT:
                self.color_display.color(Red())
            elif self.category == BookCategory.CHILDRENS_BOOKS:
                self.color_display.color(Yellow())
            else:
                self.color_display.reset()
                return
            print(text or self.category.name)
            self.color_display.reset()

    def reset(self):
        if self.color_display:
            self.color_display.reset()
