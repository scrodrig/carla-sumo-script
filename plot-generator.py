import argparse
from util.reader import load_dataset
from loguru import logger
from util.filter import filter_by_column, filter_carla_id_by_lowest_distances
from util.plotting import plot_coordinates

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
    carla_ego_dataframe = filter_by_column(all_dataframe, "Role", "hero")
    filter_carla_id_by_lowest_distances(nearby_dataframe, 3)
    plot_coordinates(carla_ego_dataframe, ego_title="hero")



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
    arguments = argparser.parse_args()

    main()
