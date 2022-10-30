def singleton(cls):
    instances_lookup = dict()

    def wrapper(*args, **kwargs):
        if cls not in instances_lookup:
            instances_lookup[cls] = cls(*args, **kwargs)
        return instances_lookup[cls]

    return wrapper
