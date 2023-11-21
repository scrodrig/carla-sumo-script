import matplotlib.pyplot as plotter
from util.color import PlotColor
from loguru import logger
from util.physics import calculate_total_distance


def plot_coordinates(df, x_key="Carla X", y_key="Carla Y", ego_title="ego"):
    """
    Plots the x and y coordinates from a given data frame.

    Parameters:
    df (pandas.DataFrame): The data frame containing the x and y coordinates.
    x_key (str, optional): The column name for the x coordinates. Defaults to 'Carla X'.
    y_key (str, optional): The column name for the y coordinates. Defaults to 'Carla Y'.
    ego_title (str, optional): The title for the plot. Defaults to 'hero'.

    Returns:
    None
    """
    logger.info("Retrieving values for: {} and {}".format(x_key, y_key))
    x = df[x_key]
    y = df[y_key]

    logger.info("Calculating total distance of {} journey".format(ego_title.upper()))
    total_distance = calculate_total_distance(df)
    logger.warning(
        "Total distance of {} journey: {} meters".format(
            ego_title.upper(), total_distance
        )
    )

    logger.info("Configuring plotter for {}".format(ego_title.upper()))
    plotter.xlabel("X")
    plotter.ylabel("Y")
    plotter.grid(True)
    plotter.axis("equal")
    logger.warning("Start plotting for {} vehicle journey".format(ego_title.upper()))
    plotter.title(
        "{} vehicle journey - Distance: {:.2f} meters".format(
            ego_title.upper(), total_distance
        )
    )

    # Set the line width and color
    plotter.plot(x, y, linewidth=0.5, color=PlotColor.BLUE)

    plotter.show()
    logger.warning("End plotting for {} vehicle journey".format(ego_title.upper()))
