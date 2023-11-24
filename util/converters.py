def convert_seconds(seconds):
    """
    Converts the given number of seconds into minutes and remaining seconds.

    Args:
      seconds (int): The number of seconds to convert.

    Returns:
      tuple: A tuple containing the number of minutes and remaining seconds.
    """
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds
