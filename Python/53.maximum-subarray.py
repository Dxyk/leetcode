from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6

        :param nums: the int array
        :return: the maximum sum within a contiguous subarray
        """
        if not nums:
            return 0
        return self.dp_soln(nums)

    def dp_soln(self, nums: List[int]) -> int:
        """
        T: O(n)
        The DP solution

        :param nums: the int array
        :return: the maximum sum within a contiguous subarray
        """
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            # This is the tricky part:
            # We have two choices when we're at an index
            # 1. We extend the current subarray and add the num
            # 2. We start from the current index and form a new subarray
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def two_pointer_quadratic_soln(self, nums: List[int]) -> int:
        """
        T: O(n^2)
        The two pointer quadratic solution: improve brute force soln by memorizing the previous sums

        :param nums: the int array
        :return: the maximum sum within a contiguous subarray
        """
        left, right = 0, 1
        max_sum = None
        while left < len(nums) - 1:  # O(n)
            right = left + 1
            curr_sum = 0
            while right < len(nums):  # O(n)
                curr_sum += nums[right - 1]
                if not max_sum or curr_sum > max_sum:
                    max_sum = curr_sum
                right += 1
            left += 1
        return max_sum

    def two_pointer_brute_force_soln(self, nums: List[int]) -> int:
        """
        T: O(n^3)
        The two pointer brute force solution

        :param nums: the int array
        :return: the maximum sum within a contiguous subarray
        """
        left, right = 0, 1
        max_sum = None
        while left < len(nums) - 1:  # O(n)
            right = left + 1
            while right < len(nums):  # O(n)
                curr_sum = sum(nums[left: right])  # O(n)
                if not max_sum or curr_sum > max_sum:
                    max_sum = curr_sum
                right += 1
            left += 1
        return max_sum
