from exceptions import IntegerException, InvalidRangeException, NegativeNumberException


def validate_input(func):
    def wrapper_func(*args, **kwargs):
        for arg in args[1:]:
            if not isinstance(arg, int):
                raise IntegerException

            if arg < 0:
                raise NegativeNumberException

        if len(args[1:]) == 2:
            num1, num2 = args[1:]
            if num1 > num2:
                raise InvalidRangeException

        return func(*args, **kwargs)

    return wrapper_func
