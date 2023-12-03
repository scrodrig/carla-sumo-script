from loguru import logger
import warnings
from datetime import datetime

import pandas as pd

from util.physics import calculate_total_distance


def number_of_records(pd_dataframe):
    return pd_dataframe.shape[0]


def seconds_difference(pd_dataframe):
    first_record = pd_dataframe.iloc[0]
    last_record = pd_dataframe.iloc[-1]
    return last_record["time"] - first_record["time"]



def closest_point(ergo_dataframe, nearby_record):
    ergo_copy_df = ergo_dataframe.copy()
    ergo_copy_df["delay"] = abs(ergo_dataframe["time"] - nearby_record.iloc[0]["time"])
    return ergo_copy_df.sort_values(by=["delay"]).head(1)


def closest_records(ergo_dataframe, timestamp, num_records=3):
    closest_records = ergo_dataframe.iloc[
        (ergo_dataframe["time"] - timestamp).abs().argsort()[:num_records]
    ]
    return closest_records


def seconds_difference_delay(first_record, last_record):
    dt_last = datetime.fromtimestamp(last_record["time"])
    dt_first = datetime.fromtimestamp(first_record["time"])
    return abs(dt_last - dt_first).total_seconds() * 1000


def average_velocity(pd_dataframe):
    distance = calculate_total_distance(pd_dataframe)
    seconds = seconds_difference(pd_dataframe)
    return distance / seconds

