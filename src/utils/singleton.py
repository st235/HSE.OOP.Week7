import inspect
from functools import wraps


def singleton(cls):
    """
    Creates a singleton for the given class.
    All tries to create an object will result in
    returning the same instance.

    @singleton
    class MyClass

    a = MyClass()
    b = MyClass()

    a should be equal to b

    :param cls: singleton will be created for this class
    :return: a singleton instance
    """
    if not inspect.isclass(cls):
        raise Exception('@singleton cannot be applied only to classes')

    instances_lookup = dict()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances_lookup:
            instances_lookup[cls] = cls(*args, **kwargs)
        return instances_lookup[cls]

    return wrapper
