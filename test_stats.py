from typing import Dict, Set

import pytest

from main import Stats


@pytest.fixture
def data():
    nums_count = {3: 2, 4: 1, 6: 1, 9: 1}
    unique_nums = {3, 4, 6, 9}
    return nums_count, unique_nums


def test_less(data):
    stats = Stats(*data)
    assert stats.less(5) == 3
    assert stats.less(10) == 5
    assert stats.less(1000) == 5
    assert stats.less(1) == 0


def test_between(data):
    stats = Stats(*data)
    assert stats.between(3, 6) == 4
    assert stats.between(6, 9) == 2


def test_greater(data):
    stats = Stats(*data)
    assert stats.greater(5) == 2
    assert stats.greater(10) == 0
    assert stats.greater(1) == 5


def test_first_num_greater_than_second_num(data):
    stats = Stats(*data)
    with pytest.raises(ValueError):
        stats.between(10, 5)
