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
  logger.info("Number of records with {} = {}: {}".format(column_name, value, filtered_df.shape[0]))
  return filtered_df

