from collections import defaultdict
from typing import Dict

from exceptions import NoDataAvailableException
from stats import Stats
from validations import validate_input


class DataCapture:
    """
    Data capture class to capture the data and generate stats
    """

    def __init__(self):
        """
        Initialize the data capture object
        """
        self.__nums: Dict[int, int] = defaultdict(int)
        self.__max_num = 0

    @validate_input
    def add(self, num: int) -> None:
        """
        Add a number to the data capture object
        :param num:
        :return: None
        """

        self.__nums[num] += 1
        self.__max_num = max(self.__max_num, num)

    def build_stats(self) -> Stats:
        """
        Build stats object
        :return: stats object
        """

        if not self.__nums:
            raise NoDataAvailableException

        return Stats(self.__nums, self.__max_num)
