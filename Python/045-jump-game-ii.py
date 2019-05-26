from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given an array of non-negative integers, you are initially positioned at the first index
        of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        Note:
        - You can assume that you can always reach the last index.

        >>> Solution().jump([2, 3, 1, 1, 4])
        2

        :param nums: the numbers of steps allowed at each index
        :return: the minimum numbers needed to reach the end of the list
        """
        if len(nums) <= 1:
            return 0
        return self.brute_force(nums)

    def brute_force(self, nums: List[int]) -> int:
        """
        T: O()
        The brute force solution

        :param nums: the numbers of steps allowed at each index
        :return: the minimum numbers needed to reach the end of the list
        """


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
