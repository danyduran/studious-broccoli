from collections import defaultdict
from queue import PriorityQueue
from typing import Dict

from exceptions import (
    InvalidInputException,
    NegativeNumberException,
    NoDataAvailableException,
)
from stats import Stats


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
