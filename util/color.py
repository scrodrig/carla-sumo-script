import random
import matplotlib.colors as mcolors


class PlotColor:
    RED = "red"
    DODGERBLUE = "dodgerblue"
    GREEN = "green"
    ORANGE = "orange"
    PURPLE = "purple"
    MAGENTA = "magenta"
    YELLOW = "yellow"

    def get_random_color():
        colors = [color for color in dir(PlotColor) if not color.startswith("__")]
        return random.choice(colors)
