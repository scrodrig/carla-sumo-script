import pandas as pd
import numpy as np
from loguru import logger


def __calculate_distance(df):
    """
    Calculates the distance between each row in the DataFrame and adds a cumulative distance column.

    Args:
      df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
      pandas.DataFrame: The DataFrame with the distance and cumulative distance columns added.
    """

    df_distance = pd.DataFrame()  # Define df_distance DataFrame
    logger.info("Calculate the distance between each row")
    df_distance["distance"] = np.sqrt(
        (df["Carla X"].diff() ** 2)
        + (df["Carla Y"].diff() ** 2)
        + (df["Carla Z"].diff() ** 2)
    )

    return df_distance


def calculate_total_distance(df):
    """
    Calculates the total distance traveled based on the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the distance data.

    Returns:
    float: The total distance traveled.
    """

    logger.info("Calculate the distance between each row")
    df_distance = __calculate_distance(df)
    logger.info("Calculate the summation of the distance between each row")
    total_distance = df_distance["distance"].sum()

    return total_distance
