import random
from enum import Enum
import matplotlib.colors as mcolors


class PlotColor:
    RED = "red"
    DODGERBLUE = "dodgerblue"
    BLUE = "blue"
    DARKSEAGREEN = "darkseagreen"
    GREEN = "green"
    BLACK = "black"
    MAGENTA = "magenta"
    GOLD  = "gold"
    ORANGE = "orange"
    LIME = "lime"
    FIREBRICK = "firebrick"
    DARKMAGENTA = "darkmagenta"


def get_random_color():
    """
    Returns a random color from the available colors.

    Returns:
    - A random color from the available colors.
    - If no colors are available, returns PlotColor.RED.
    """
    colors = [color for color in dir(PlotColor) if not color.startswith("__")]
    return random.choice(colors)

