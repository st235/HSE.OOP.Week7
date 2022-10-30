import datetime as dt


def get_current_time():
    return get_time(dt.datetime.now())

def get_time(datetime):
    return datetime.hour * 60 + datetime.minute