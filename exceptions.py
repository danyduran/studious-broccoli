class NegativeNumberException(Exception):
    """Negative numbers are not allowed"""
    pass


class InvalidInputException(Exception):
    """Only integers are allowed"""
    pass


class NoDataAvailableException(Exception):
    """No data available to build stats"""
    pass


class InvalidRangeException(Exception):
    """First number should be less than second number"""
    pass


class NegativeIndexException(Exception):
    """Negative index is not allowed"""
    pass
