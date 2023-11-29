from collections import defaultdict
from typing import List, Set, Dict


class Stats:
    """
    this class is used to build stats from the data capture object

    """

    def __init__(self, nums: Dict[int, int], unique_nums: Set[int]):
        self.__nums = nums
        self.__unique_nums = sorted(unique_nums)

        self.__prefix_sum = self.__build_prefix_sum()

    def __build_prefix_sum(self) -> List[int]:
        """
        Build prefix sum and indexes
        Time Complexity: O(n)
        :return:
        """
        prefix_sum = [0] * (max(self.__unique_nums) + 1)

        for index in range(1, len(prefix_sum)):
            prefix_sum[index] = (prefix_sum[index - 1] + self.__nums.get(index, 0))

        return prefix_sum

    def less(self, num: int) -> int:
        """
        Return the number of elements less than num
        Time Complexity: O(1)
        :param num:
        :return:
        """
        if num >= len(self.__prefix_sum):
            return self.__prefix_sum[-1]

        return self.__prefix_sum[num - 1]

    def between(self, num1: int, num2: int) -> int:
        """
        Return the number of elements between num1 and num2
        Time Complexity: O(1)
        :param num1:
        :param num2:
        :return:
        """

        return self.__prefix_sum[num2] - self.__prefix_sum[(num1 - 1)]

    def greater(self, num: int) -> int:
        """
        Return the number of elements greater than num
        Time Complexity: O(1)
        :param num:
        :return:
        """

        if num >= len(self.__prefix_sum):
            return 0

        return self.between(num + 1, self.__unique_nums[-1])


class DataCapture:
    """
    this class is used to capture data, the only purpose is capture data
    this class is not responsible for any other functionality
    following the single responsibility principle
    """

    def __init__(self):
        self.__nums: Dict[int, int] = defaultdict(int)
        self.__unique_nums: Set[int] = set()

    def add(self, num: int):
        """
        Adds a number to the data capture object
        Time Complexity: O(1)
        :param num:
        :return:
        """
        if num < 0:
            raise ValueError("Negative numbers are not allowed")

        self.__nums[num] += 1
        self.__unique_nums.add(num)

    def build_starts(self) -> Stats:
        """
        Generate stats from the data capture object
        :return:
        """
        return Stats(self.__nums, self.__unique_nums)


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(4)
    capture.add(5)
    capture.add(6)
    capture.add(6)
    capture.add(9)

    stats = capture.build_starts()
    assert stats.less(4) == 2
    assert stats.between(3, 6) == 7
    assert stats.greater(4) == 4
