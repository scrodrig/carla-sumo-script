"""
Class to load csv into datasets
"""
from loguru import logger
from pathlib import Path
import pandas as pd


cols_all = [
    "CarlaId",
    "SumoId",
    "Model",
    "Role",
    "Carla X",
    "Carla Y",
    "Carla Z",
    "SUMO X",
    "SUMO Y",
    "SUMO Z",
    "time",
]

cols_nearby = [
    "CarlaId",
    "Name",
    "Model",
    "Role",
    "Distance",
    "Carla X",
    "Carla Y",
    "Carla Z",
    "time",
]


def load_dataset(csv_name, event_file=True):
    """Load_dataset opens a csv and returns a DataSet"""
    # This second parent is because we are inside `util`
    HERE = Path(__file__).parent.parent
    INPUT_FOLDER = HERE / "input"
    logger.info("{}: {}".format("PATH TO FILE", INPUT_FOLDER / csv_name))

    colums = cols_all if event_file else cols_nearby

    dataframe_read = pd.read_csv(
        INPUT_FOLDER / csv_name,
        encoding="unicode_escape",
        converters={"Model": str.lower, "Role": str.lower},
        usecols=colums,
    )

    logger.info(
        "{} OF {}: {}".format("NUMBER OF RECORDS", csv_name, dataframe_read.shape[0])
    )

    return dataframe_read
