import pytest
from main import DataCapture, Stats


@pytest.fixture
def data_capture():
    capture = DataCapture()
    nums = [3, 3, 4, 6, 9]
    for num in nums:
        capture.add(num)
    return capture


def test_create_build_stats(data_capture):
    stats = data_capture.build_starts()
    assert Stats == type(stats)


@pytest.mark.parametrize("negative_number", [-2, -3, -4, -5])
def test_negative_number_add(data_capture, negative_number):
    with pytest.raises(ValueError):
        data_capture.add(negative_number)
