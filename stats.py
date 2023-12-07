from typing import Dict, List

from exceptions import InvalidRangeException
from validations import only_integer, only_positive


class Stats:
    """
    Stats class to calculate the number of elements less than, between and greater than a given number
    """

    def __init__(self, nums: Dict[int, int], max_num: int):
        """
        Initialize the stats object
        :param nums:
        :param max_num:
        """
        self.__nums = nums
        self.__max_num = max_num

        self.__prefix_sum = self.__build_prefix_sum()

    def __build_prefix_sum(self) -> List[int]:
        """
        Build prefix sum array
        :return: prefix sum array
        """
        prefix_sum = [0] * (self.__max_num + 1)

        for index in range(1, len(prefix_sum)):
            prefix_sum[index] = prefix_sum[index - 1] + self.__nums.get(index, 0)

        return prefix_sum

    @only_positive
    @only_integer
    def less(self, num: int) -> int:
        """
        Return the number of elements less than num
        Time Complexity: O(1)
        :param num:
        :return: number of elements less than num
        """

        if num >= len(self.__prefix_sum):
            return self.__prefix_sum[-1]

        return self.__prefix_sum[num - 1]

    @only_positive
    @only_integer
    def between(self, num1: int, num2: int) -> int:
        """
        Return the number of elements between num1 and num2
        Time Complexity: O(1)
        :param num1:
        :param num2:
        :return: number of elements between num1 and num2
        """
        if num1 > num2 or num1 > self.__max_num or num2 > self.__max_num:
            raise InvalidRangeException
        return self.__prefix_sum[num2] - self.__prefix_sum[(num1 - 1)]

    @only_positive
    @only_integer
    def greater(self, num: int) -> int:
        """
        Return the number of elements greater than num
        Time Complexity: O(1)
        :param num:
        :return: number of elements greater than num
        """
        if num >= len(self.__prefix_sum):
            return 0

        return self.between(num + 1, self.__max_num)
