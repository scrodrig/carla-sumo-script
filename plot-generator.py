import argparse
from util.reader import load_dataset
from loguru import logger
from util.filter import (
    filter_by_column,
    filter_carla_id_by_lowest_distances,
    __get_nearby_carla_ids,
)
from util.plotting import (
    plot_coordinates_individual,
    nearby_individual_plotting,
    plot_nearby_individual_vehicles,
    plot_all_nearby_vehicles,
)
from util.color import PlotColor


def main():
    """
    Entry point of the script. Generates plots for Carla-Sumo data.

    This method loads the dataset, filters the data, and generates plots based on the filtered data.

    Args:
        None

    Returns:
        None
    """
    logger.critical("Carla-Sumo - Script plot generation")
    all_dataframe = load_dataset(arguments.csv_file)
    nearby_dataframe = load_dataset(arguments.nearby_csv_file, event_file=False)
    carla_ego_dataframe = filter_by_column(all_dataframe, "Role", arguments.ego_name)
    plot_coordinates_individual(
        carla_ego_dataframe, title=arguments.ego_name, linewidth=0.5
    )

    # Plot the nearby vehicles
    nearby_vehicles_dataframe = filter_carla_id_by_lowest_distances(
        nearby_dataframe, arguments.nearby_vehicles
    )
    nearby_vehicles_ids = __get_nearby_carla_ids(
        nearby_vehicles_dataframe, arguments.nearby_vehicles
    )
    if arguments.nearby_individual_plotting:
        nearby_individual_plotting(all_dataframe, nearby_vehicles_ids)

    if arguments.nearby_ego_plotting:
        plot_nearby_individual_vehicles(
            all_dataframe,
            x_key="Carla X",
            y_key="Carla Y",
            ego_name=arguments.ego_name,
            nearby_dataframe=nearby_vehicles_dataframe,
            nearby_vehicles_ids=nearby_vehicles_ids,
        )

    plot_all_nearby_vehicles(
        all_dataframe,
        x_key="Carla X",
        y_key="Carla Y",
        ego_name=arguments.ego_name,
        nearby_dataframe=nearby_vehicles_dataframe,
        nearby_vehicles_ids=nearby_vehicles_ids,
    )


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--csv-file",
        type=str,
        help="all events csv file",
    )
    argparser.add_argument(
        "--nearby-csv-file",
        type=str,
        help="nearby csv file for all events",
    )
    argparser.add_argument(
        "--nearby-vehicles",
        type=int,
        help="number of vehicles nearby to plot",
        default=3,
    )
    argparser.add_argument(
        "--ego-name",
        type=str,
        help="name of the ego vehicle, g.e. hero",
        default="ego",
    )
    argparser.add_argument(
        "--nearby-individual-plotting",
        type=bool,
        help="Need to see the individual plotting for nearby vehicles?",
        default=False,
    )
    argparser.add_argument(
        "--nearby-ego-plotting",
        type=bool,
        help="Need to see the individual plotting for nearby vehicles with ego?",
        default=False,
    )
    arguments = argparser.parse_args()

    main()
