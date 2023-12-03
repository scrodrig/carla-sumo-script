import matplotlib.pyplot as plotter
from util.color import PlotColor, get_random_color
from loguru import logger
from util.physics import calculate_total_distance
from util.filter import filter_by_column, get_lowest_time
from util.converters import convert_seconds
from util.stats import seconds_difference


def plot_coordinates_individual(
    df,
    x_key="Carla X",
    y_key="Carla Y",
    title="ego",
    color=PlotColor.DODGERBLUE,
    linewidth=1.0,
):
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
    logger.warning("Start plotting for {} vehicle journey".format(plot_title))

    logger.info("Retrieving values for: {} and {}".format(x_key, y_key))
    x = df[x_key]
    y = df[y_key]

    logger.info("Calculating total distance of {} journey".format(plot_title))
    total_distance = calculate_total_distance(df)
    logger.warning(
        "Total distance of {} journey: {} meters".format(plot_title, total_distance)
    )

    logger.info("Configuring plotter for {}".format(plot_title))
    plotter.xlabel("X")
    plotter.ylabel("Y")
    # plotter.grid(True)
    plotter.axis("equal")
    plotter.title(
        "Vehicle {}'s journey - Distance: {:.2f} meters".format(
            plot_title, total_distance
        )
    )

    # Set the line width and color
    plotter.plot(x, y, linewidth=linewidth, color=color)

    plotter.show()
    logger.warning("End plotting for {} vehicle journey".format(plot_title))


def nearby_individual_plotting(all_dataframe, nearby_vehicles_ids):
    """
    Plot individual nearby vehicles based on their CarlaId.

    Parameters:
    all_dataframe (pandas.DataFrame): The dataframe containing all vehicle data.
    nearby_vehicles_ids (list): A list of CarlaIds of nearby vehicles.

    Returns:
    None
    """
    for carla_id in nearby_vehicles_ids:
        nearby_vehicle_dataframe = filter_by_column(all_dataframe, "CarlaId", carla_id)
        plot_coordinates_individual(
            nearby_vehicle_dataframe, title=carla_id, color=get_random_color()
        )


def plot_nearby_individual_vehicles(
    df,
    x_key="Carla X",
    y_key="Carla Y",
    ego_name="ego",
    nearby_vehicles_ids=[],
    nearby_dataframe=None,
    color_ego=PlotColor.DODGERBLUE,
    color_nearby=PlotColor.RED,
    linewidth=1.0,
):
    """
    Plots the journey of nearby individual vehicles.

    Args:
        df (DataFrame): The main dataframe containing the vehicle data.
        x_key (str, optional): The column name for the x-coordinate. Defaults to "Carla X".
        y_key (str, optional): The column name for the y-coordinate. Defaults to "Carla Y".
        ego_name (str, optional): The name of the ego vehicle. Defaults to "ego".
        nearby_vehicles_ids (list, optional): The list of nearby vehicle IDs. Defaults to [].
        nearby_dataframe (DataFrame, optional): The dataframe containing the nearby vehicle data. Defaults to None.
        color_ego (str, optional): The color for plotting the ego vehicle. Defaults to PlotColor.DODGERBLUE.
        color_nearby (str, optional): The color for plotting the nearby vehicles. Defaults to PlotColor.RED.
        linewidth (float, optional): The linewidth for the plotted lines. Defaults to 1.0.
    """

    logger.debug("Start plotting for nearby individual vehicles journey")
    first_record_time = get_lowest_time(df)
    carla_ego_dataframe = filter_by_column(df, "Role", ego_name)

    for carla_id in nearby_vehicles_ids:
        logger.warning(
            "Start sub-plotting for {} - {} vehicle journey".format(ego_name, carla_id)
        )
        logger.info(
            "Retrieving values for: {} and {} in {}".format(x_key, y_key, ego_name)
        )
        x = carla_ego_dataframe[x_key]
        y = carla_ego_dataframe[y_key]
        logger.info(
            "Retrieving values for: {} and {} in {}".format(x_key, y_key, carla_id)
        )
        nearby_vehicle_dataframe = filter_by_column(df, "CarlaId", carla_id)
        nearby_x = nearby_vehicle_dataframe[x_key]
        nearby_y = nearby_vehicle_dataframe[y_key]

        # Select a record based on a specific value in a column
        selected_record = nearby_dataframe.loc[nearby_dataframe["CarlaId"] == carla_id]
        time_in_test = selected_record.iloc[0]["time"] - first_record_time
        minutes, seconds = convert_seconds(time_in_test)

        plotter.suptitle(
            "Vehicle {} - {} journey - Comparation - ~ {:.2f} meters".format(
                ego_name, carla_id, selected_record["Distance"].values[0]
            )
        )

        plotter.plot(
            selected_record.iloc[0]["Carla X"],
            selected_record.iloc[0]["Carla Y"],
            label="Clst. distance",
            marker="o",
            markersize=5,
            markeredgecolor=PlotColor.BLACK,
            markerfacecolor=PlotColor.GREEN,
        )
        plotter.plot(x, y, label=ego_name, color=color_ego)
        plotter.plot(nearby_x, nearby_y, label=carla_id, color=color_nearby)
        plotter.title(
            "Closest point at {:.0f}:{:.2f} min".format(minutes, seconds), fontsize=8
        )
        logger.info("Closest point at {:.0f}:{:.2f} min".format(minutes, seconds))
        plotter.legend()
        plotter.show()
        logger.warning(
            "End plotting for {} - {} vehicle journey".format(ego_name, carla_id)
        )
    logger.debug("End plotting for {} - {} vehicle journey".format(ego_name, carla_id))


def plot_all_nearby_vehicles(
    df,
    x_key="Carla X",
    y_key="Carla Y",
    ego_name="ego",
    nearby_vehicles_ids=[],
    nearby_dataframe=None,
    color_ego=PlotColor.DODGERBLUE,
):
    """
    Plot the journey of the ego vehicle and all nearby vehicles.

    Args:
        df (DataFrame): The main dataframe containing the vehicle data.
        x_key (str, optional): The column name for the x-coordinate of the vehicles. Defaults to "Carla X".
        y_key (str, optional): The column name for the y-coordinate of the vehicles. Defaults to "Carla Y".
        ego_name (str, optional): The name of the ego vehicle. Defaults to "ego".
        nearby_vehicles_ids (list, optional): The list of nearby vehicle IDs. Defaults to an empty list.
        nearby_dataframe (DataFrame, optional): The dataframe containing the nearby vehicle data. Defaults to None.
        color_ego (str, optional): The color of the ego vehicle plot. Defaults to PlotColor.DODGERBLUE.
    """
    logger.warning("Start plotting for ALL nearby vehicles journey")
    logger.info("Retrieving values for: {} and {} in {}".format(x_key, y_key, ego_name))
    carla_ego_dataframe = filter_by_column(df, "Role", ego_name)

    logger.info("Retrieving values for: {} and {} in {}".format(x_key, y_key, ego_name))
    x = carla_ego_dataframe[x_key]
    y = carla_ego_dataframe[y_key]
    plotter.plot(x, y, label=ego_name, color=color_ego)

    for carla_id in nearby_vehicles_ids:
        logger.info(
            "Retrieving values for: {} and {} in {}".format(x_key, y_key, carla_id)
        )
        nearby_vehicle_dataframe = filter_by_column(df, "CarlaId", carla_id)
        nearby_x = nearby_vehicle_dataframe[x_key]
        nearby_y = nearby_vehicle_dataframe[y_key]

        # Select a record based on a specific value in a column
        selected_record = nearby_dataframe.loc[nearby_dataframe["CarlaId"] == carla_id]

        color_nearby = get_random_color()

        plotter.plot(nearby_x, nearby_y, label=carla_id, color=color_nearby)
        plotter.plot(
            selected_record.iloc[0]["Carla X"],
            selected_record.iloc[0]["Carla Y"],
            marker="o",
            markersize=5,
            markeredgecolor=PlotColor.BLACK,
            markerfacecolor=color_nearby,
        )

    plotter.title("All nearby vehicles")
    plotter.legend()
    plotter.show()
    logger.warning("End plotting for ALL nearby vehicles journey")



