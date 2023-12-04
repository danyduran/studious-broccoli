import pytest

from data_capture import DataCapture
from exceptions import (
    InvalidInputException,
    NegativeNumberException,
    NoDataAvailableException,
)
from stats import Stats


@pytest.fixture
def data_capture():
    capture = DataCapture()
    nums = [3, 3, 4, 6, 9]
    for num in nums:
        capture.add(num)
    return capture


def test_create_build_stats(data_capture):
    stats = data_capture.build_stats()
    assert Stats == type(stats)


@pytest.mark.parametrize("invalid_input", ["foo", "bar", 34 + 1j])
def test_type_error_add(data_capture, invalid_input):
    with pytest.raises(InvalidInputException):
        data_capture.add(invalid_input)


@pytest.mark.parametrize("negative_number", [-2, -3, -4, -5])
def test_negative_number_add(data_capture, negative_number):
    with pytest.raises(NegativeNumberException):
        data_capture.add(negative_number)


def test_not_data_build_stats():
    capture = DataCapture()
    with pytest.raises(NoDataAvailableException):
        capture.build_stats()
