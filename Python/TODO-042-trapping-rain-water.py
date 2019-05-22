from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1
        compute how much water it is able to trap after raining.

        See image https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
        where [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], and 6 units of water are trapped

        >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6

        :param height: a list that represents the elevation map
        :return: the number of units of rain water being trapped
        """
        return self.stack_soln(height)

    def stack_soln(self, height: List[int]) -> int:
        """
        T: O()

        :param height: a list that represents the elevation map
        :return: the number of units of rain water being trapped
        """


if __name__ == '__main__':
    Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
