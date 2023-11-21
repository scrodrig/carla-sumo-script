import argparse
from util.reader import load_dataset
from loguru import logger

"""
Entry point to the plot generator
"""


def main():
    logger.critical("Carla-Sumo - Script plot generation")
    all_dataset = load_dataset(arguments.csv_file)
    nearby_dataset = load_dataset(arguments.nearby_csv_file, event_file=False)


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
