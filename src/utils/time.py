import datetime as dt


def get_current_time():
    current_time = dt.datetime.now()
    return current_time.hour * 60 + current_time.minute
