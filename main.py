from collections import defaultdict
from queue import PriorityQueue
from typing import Dict, List

from exceptions import (
    InvalidInputException,
    InvalidRangeException,
    NegativeIndexException,
    NegativeNumberException,
    NoDataAvailableException,
)


class Stats:
    """
    Stats class to calculate the number of elements less than, between and greater than a given number
    """

    def __init__(self, nums: Dict[int, int], unique_nums: List[int]):
        """
        Initialize the stats object
        :param nums:
        :param unique_nums:
        """
        self.__nums = nums
        self.__unique_nums = unique_nums

        self.__prefix_sum = self.__build_prefix_sum()

    def __build_prefix_sum(self) -> List[int]:
        """
        Build prefix sum array
        :return: prefix sum array
        """
        prefix_sum = [0] * (self.__unique_nums[-1] + 1)

        for index in range(1, len(prefix_sum)):
            prefix_sum[index] = prefix_sum[index - 1] + self.__nums.get(index, 0)

        return prefix_sum

    def less(self, num: int) -> int:
        """
        Return the number of elements less than num
        Time Complexity: O(1)
        :param num:
        :return: number of elements less than num
        """

        if num < 0:
            raise NegativeIndexException

        if num >= len(self.__prefix_sum):
            return self.__prefix_sum[-1]

        return self.__prefix_sum[num - 1]

    def between(self, num1: int, num2: int) -> int:
        """
        Return the number of elements between num1 and num2
        Time Complexity: O(1)
        :param num1:
        :param num2:
        :return: number of elements between num1 and num2
        """
        if num1 < 0 or num2 < 0:
            raise NegativeIndexException

        if num1 > num2:
            raise InvalidRangeException

        return self.__prefix_sum[num2] - self.__prefix_sum[(num1 - 1)]

    def greater(self, num: int) -> int:
        """
        Return the number of elements greater than num
        Time Complexity: O(1)
        :param num:
        :return: number of elements greater than num
        """

        if num < 0:
            raise NegativeIndexException

        if num >= len(self.__prefix_sum):
            return 0

        return self.between(num + 1, self.__unique_nums[-1])


class DataCapture:
    """
    Data capture class to capture the data and generate stats
    """

    def __init__(self):
        """
        Initialize the data capture object
        """
        self.__nums: Dict[int, int] = defaultdict(int)
        self.__unique_nums: PriorityQueue = PriorityQueue()

    def add(self, num: int) -> None:
        """
        Add a number to the data capture object
        :param num:
        :return: None
        """

        if not isinstance(num, int):
            raise InvalidInputException

        if num < 0:
            raise NegativeNumberException

        if num not in self.__nums:
            self.__unique_nums.put(num)

        self.__nums[num] += 1

    def build_stats(self) -> Stats:
        """
        Build stats object
        :return: stats object
        """

        if not self.__nums:
            raise NoDataAvailableException

        return Stats(self.__nums, self.__unique_nums.queue)


if __name__ == "__main__":
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(4)
    capture.add(5)
    capture.add(6)
    capture.add(6)
    capture.add(9)

    stats = capture.build_stats()
    assert stats.less(4) == 2
    assert stats.between(3, 6) == 7
    assert stats.greater(4) == 4
