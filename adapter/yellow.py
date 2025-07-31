from adapter.icolor import IColor

class Yellow(IColor):
    def color_console(self) -> str:
        print("\033[93m", end="")  # צהוב
        return "yellow"
