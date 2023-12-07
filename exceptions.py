class NegativeNumberException(Exception):
    """Negative numbers/indexes are not allowed"""

    pass


class IntegerException(Exception):
    """Only integers are allowed"""

    pass


class NoDataAvailableException(Exception):
    """No data available to build stats"""

    pass


class InvalidRangeException(Exception):
    """First number should be less than second number"""

    pass
