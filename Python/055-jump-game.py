from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Given an array of non-negative integers, you are initially positioned at the first index
        of the array.

        Each element in the array represents your maximum jump length at that position.

        Determine if you are able to reach the last index.

        >>> Solution().canJump([2, 3, 1, 1, 4])
        True
        >>> Solution().canJump([3, 2, 1, 0, 4])
        False

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """

    def brute_force(self, nums: List[int]) -> bool:
        """
        T: O()
        The brute force soln

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """
        max_step = nums[0]
        for idx in range(1, len(nums)):
            if idx > max_step:
                return False
