import datetime as dt


def get_current_time() -> int:
    """
    Gets system's 'wall' time of the day in minutes.

    :return: current time of the day in minutes
    """
    return get_time(dt.datetime.now())


def get_time(datetime) -> int:
    """
    Converts the given datetime to time of day in minutes.
    Result is calculated by the following formula: hours * 60 + minutes

    :return: time of the day in minutes
    """
    return datetime.hour * 60 + datetime.minute


def get_hours_and_minutes(time: int) -> (int, int):
    """
    Returns a tuple of hours, minutes for the given integer time of the day
    """
    max_time = 24 * 60

    return (time % max_time) // 60, (time % max_time) % 60
