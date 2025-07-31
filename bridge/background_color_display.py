from bridge.color_display import ColorDisplay
from adapter.icolor import IColor

class BackgroundColorDisplay(ColorDisplay):
    def __init__(self):
        self._color = None

    def color(self, color: IColor):
        self._color = color.color_console()

    def display(self):
        print(f"[BackgroundColorDisplay] Displaying background in color: {self._color}")

    def reset(self):
        print("\033[0m", end="")  # איפוס צבעים
