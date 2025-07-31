from adapter.icolor import IColor

class Blue(IColor):
    def color_console(self) -> str:
        print("\033[94m", end="")  # כחול
        return "blue"
