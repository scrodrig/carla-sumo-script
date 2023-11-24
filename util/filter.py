import pandas as pd
from loguru import logger


def filter_by_column(df, column_name, value):
    """
    Filter a DataFrame by a specific column and value.

    Parameters:
      df (pandas.DataFrame): The DataFrame to be filtered.
      column_name (str): The name of the column to filter by.
      value: The value to filter the column by.

    Returns:
      pandas.DataFrame: The filtered DataFrame.

    """
    logger.info("Filtering by column: {} with value: {}".format(column_name, value))
    filtered_df = df[df[column_name] == value]
    logger.info(
        "Number of records with {} = {}: {}".format(
            column_name, value, filtered_df.shape[0]
        )
    )
    return filtered_df


def filter_carla_id_by_lowest_distances(df, num_records):
    """
    Filter the CarlaID for the first unique three who have the lowest distances.

    Parameters:
      df (pandas.DataFrame): The DataFrame to be filtered.
      num_records (int): The number of records to return.

    Returns:
      pandas.DataFrame: The filtered DataFrame.

    """
    # Sort the DataFrame by distances in ascending order
    logger.info("Sort the DataFrame by distances in ascending order")
    sorted_df = df.sort_values(by="Distance", ascending=True)


    logger.info(
        "Get the first {} records with different unique IDs".format(num_records)
    )
    filtered_df = sorted_df.drop_duplicates(subset="CarlaId").head(num_records)

    logger.info("Get the unique CarlaIDs with the lowest distances")
    unique_carla_ids = __get_nearby_carla_ids(filtered_df, num_records)
    
    logger.warning(
        "First {} vehicles that were closest: {}".format(num_records, unique_carla_ids)
    )

    return filtered_df


def __get_nearby_carla_ids(df, num_records):
    """
    Get the unique CarlaIDs for the nearby vehicles based on the filtered DataFrame.

    Parameters:
      df (pandas.DataFrame): The filtered DataFrame.
      num_records (int): The number of records to consider for each CarlaID.

    Returns:
      numpy.ndarray: An array of unique CarlaIDs for the nearby vehicles.

    """
    unique_carla_ids = (
        df.groupby("CarlaId").head(num_records)["CarlaId"].unique()
    )
    return unique_carla_ids
