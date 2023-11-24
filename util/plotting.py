import matplotlib.pyplot as plotter
from util.color import PlotColor
from loguru import logger
from util.physics import calculate_total_distance


def plot_coordinates_individual(df, x_key="Carla X", y_key="Carla Y", title="ego", color=PlotColor.DODGERBLUE, linewidth=1.0):
    """
    Plots the x and y coordinates from a given data frame.

    Parameters:
    df (pandas.DataFrame): The data frame containing the x and y coordinates.
    x_key (str, optional): The column name for the x coordinates. Defaults to 'Carla X'.
    y_key (str, optional): The column name for the y coordinates. Defaults to 'Carla Y'.
    title (str, optional): The title for the plot. Defaults to 'hero'.

    Returns:
    None
    """

    plot_title = title.upper() if isinstance(title, str) else title
    logger.info("Retrieving values for: {} and {}".format(x_key, y_key))
    x = df[x_key]
    y = df[y_key]

    logger.info("Calculating total distance of {} journey".format(plot_title))
    total_distance = calculate_total_distance(df)
    logger.warning(
        "Total distance of {} journey: {} meters".format(
            plot_title, total_distance
        )
    )

    logger.info("Configuring plotter for {}".format(plot_title))
    plotter.xlabel("X")
    plotter.ylabel("Y")
    plotter.grid(True)
    plotter.axis("equal")
    logger.warning("Start plotting for {} vehicle journey".format(plot_title))
    plotter.title(
        "Vehicle {}'s journey - Distance: {:.2f} meters".format(
            plot_title, total_distance
        )
    )

    # Set the line width and color
    plotter.plot(x, y, linewidth=linewidth, color=color)

    plotter.show()
    logger.warning("End plotting for {} vehicle journey".format(plot_title))

