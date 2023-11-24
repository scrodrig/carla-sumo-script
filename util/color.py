import random
import matplotlib.colors as mcolors


class PlotColor:
    RED = "red"
    DODGERBLUE = "dodgerblue"
    BLUE = "blue"
    GREEN = "green"
    ORANGE = "orange"
    BLACK = "black"

    def get_random_color():
        colors = [color for color in dir(PlotColor) if not color.startswith("__")]
        return random.choice(colors) if colors else PlotColor.RED
