from typing import Dict, List

from exceptions import InvalidRangeException, NegativeIndexException


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
