import argparse
from util.reader import load_dataset
from loguru import logger


def main():
    logger.critical("Carla-Sumo - Script plot generation")
    path = load_dataset(arguments)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--path-carla",
        type=str,
        help="path to carla file",
    )
    arguments = argparser.parse_args()

    main()
