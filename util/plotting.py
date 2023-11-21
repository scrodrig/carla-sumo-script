import matplotlib.pyplot as plotter
from util.color import PlotColor


def plot_coordinates(df, x_key="Carla X", y_key="Carla Y"):
    """
    Plots the x and y coordinates from a given data frame.

    Parameters:
    df (pandas.DataFrame): The data frame containing the x and y coordinates.
    x_key (str, optional): The column name for the x coordinates. Defaults to 'Carla X'.
    y_key (str, optional): The column name for the y coordinates. Defaults to 'Carla Y'.

    Returns:
    None
    """
    x = df[x_key]
    y = df[y_key]

    # plotter.scatter(x, y)
    plotter.xlabel("X Coordinate")
    plotter.ylabel("Y Coordinate")
    plotter.title("Plot of X and Y Coordinates")

    # Set the line width and color
    plotter.plot(x, y, linewidth=0.5, color=PlotColor.BLUE)

    plotter.show()
