import argparse
from util.reader import load_dataset 

def main():
    print("Carla-Sumo - Script plot generation")
    print("The value of __name__ is:", repr(__name__))
    path = load_dataset(arguments)
    print("==>", path)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--path-carla",
        type=str,
        help="path to carla file",
    )
    arguments = argparser.parse_args()

    main()
