from exceptions import IntegerException, NegativeNumberException


def only_positive(func):
    def wrapper_func(*args, **kwargs):
        for arg in args[1:]:
            if arg < 0:
                raise NegativeNumberException

        return func(*args, **kwargs)

    return wrapper_func


def only_integer(func):
    def wrapper_func(*args, **kwargs):
        for arg in args[1:]:
            if not isinstance(arg, int):
                raise IntegerException

        return func(*args, **kwargs)

    return wrapper_func
