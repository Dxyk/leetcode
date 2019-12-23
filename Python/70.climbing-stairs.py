#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (45.67%)
# Likes:    3031
# Dislikes: 103
# Total Accepted:    528.9K
# Total Submissions: 1.2M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp_bottom_up(n)

    def dp_bottom_up(self, n: int) -> int:
        """
        dp bottom up solution

        Runtime: O(n)
        """
        if n < 3:
            return n
        memo = [0 for _ in range(n)]
        memo[0] = 1
        memo[1] = 2
        for i in range(2, len(memo)):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]

    def dp_memoize(self, n: int) -> int:
        """
        DP memoize solution
        """
        memo = [0 for _ in range(n + 1)]

        def helper(start: int) -> int:
            if memo[start] != 0:
                return memo[start]
            res = 0
            if start == 1:
                res = 1
            elif start == 2:
                res = 2
            else:
                res = helper(start - 1) + helper(start - 2)
            memo[start] = res
            return res
        return helper(n)

    def dp_recursive(self, n: int) -> int:
        """
        DP recursive solution
        """
        def helper(start: int) -> int:
            if start == 1:
                return 1
            elif start == 2:
                return 2
            else:
                return helper(start - 1) + helper(start - 2)
        return helper(n)

# @lc code=end
