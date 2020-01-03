#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.49%)
# Likes:    3500
# Dislikes: 115
# Total Accepted:    413K
# Total Submissions: 995K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dp_bottom_up_refined_soln(nums)

    def dp_bottom_up_refined_soln(self, nums: List[int]) -> int:
        """
        DP bottom up refined solution
        Each calculation only needs i - 1 and i - 2. Thus no need for memo
        """
        prev = curr = 0
        for num in nums:
            temp = prev
            prev = curr
            curr = max(num + temp, curr)
        return curr

    def dp_bottom_up_soln(self, nums: List[int]) -> int:
        """
        DP bottom up solution
        """
        if len(nums) == 0:
            return 0
        memo = [0] * len(nums)
        memo[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                memo[i] = max(nums[i], memo[i + 1])
            else:
                memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])
        return memo[0]

    def dp_memoized_soln(self, nums: List[int]) -> int:
        """
        DP memoized solution
        """
        if len(nums) == 0:
            return 0

        memo = [None] * len(nums)

        def helper(i: int):
            if i >= len(nums):
                return 0
            if memo[i] is None:
                if i == len(nums) - 1:
                    res = nums[i]
                else:
                    res = max(nums[i] + helper(i + 2), helper(i + 1))
                memo[i] = res
            return memo[i]
        return helper(0)

    def dp_recursive_soln(self, nums: List[int]) -> int:
        """
        DP recursive solution

        Subproblem structure:
        Let P(i) := maximum amount starting from idx i
        P(i) =
            nums[i] if i > len(nums) - 2
            max(P(i + 1), nums[i] + P(i + 2)) else
        """
        if len(nums) == 0:
            return 0

        def helper(i: int):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            else:
                return max(nums[i] + helper(i + 2), helper(i + 1))
        return helper(0)
# @lc code=end


if __name__ == "__main__":
    print(Solution().rob([1, 2]), 2)
    print(Solution().rob([1, 2, 3, 1]), 4)
    print(Solution().rob([2, 7, 9, 3, 1]), 12)
