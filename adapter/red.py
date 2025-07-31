from adapter.icolor import IColor

class Red(IColor):
    def color_console(self) -> str:
        print("\033[91m", end="")  # ANSI escape code for red
        return "red"
