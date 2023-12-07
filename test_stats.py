import pytest

from exceptions import InvalidRangeException, NegativeNumberException
from stats import Stats


@pytest.fixture
def data():
    nums_count = {3: 2, 4: 1, 6: 1, 9: 1}
    max_num = 9
    return nums_count, max_num


@pytest.fixture
def stats(data):
    return Stats(*data)


@pytest.mark.parametrize("negative_num", [-1, -2, -3])
def test_negative_number_less(stats, negative_num):
    with pytest.raises(NegativeNumberException):
        stats.less(negative_num)


def test_less(stats):
    assert stats.less(5) == 3
    assert stats.less(10) == 5
    assert stats.less(1000) == 5
    assert stats.less(1) == 0


@pytest.mark.parametrize("num1, num2", [(-1, 3), (3, -1)])
def test_negative_number_between(stats, num1, num2):
    with pytest.raises(NegativeNumberException):
        stats.between(num1, num2)


@pytest.mark.parametrize("num1, num2", [(10, 3), (30, 12)])
def test_invalid_range_between(stats, num1, num2):
    with pytest.raises(InvalidRangeException):
        stats.between(num1, num2)


def test_between(stats):
    assert stats.between(3, 6) == 4
    assert stats.between(6, 9) == 2


@pytest.mark.parametrize("num", [-1, -2, -3])
def test_greater_negative_index(stats, num):
    with pytest.raises(NegativeNumberException):
        stats.greater(num)


def test_greater(stats):
    assert stats.greater(5) == 2
    assert stats.greater(10) == 0
    assert stats.greater(1) == 5
