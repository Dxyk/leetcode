#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (48.89%)
# Likes:    3607
# Dislikes: 163
# Total Accepted:    667.8K
# Total Submissions: 1.4M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.one_pass_soln(prices)

    def kadane_algo_soln(self, prices: List[int]) -> int:
        """
        Kadane's algorithm:
        calculate maximum difference by calculating maximum contiguous sum

        E.g. input: [1, 7, 4, 11]. differences: [0, 6, -3, 7]
        max_profit left: 0, right: 3
        max_curr_diff
            = in[1] - in[0] + in[2] - in[1] + in[3] - in[2]
            = in[3] - in[0]

        Runtime: O(n)
        Space: O(1)
        """
        max_curr_diff = max_profit = 0
        for i in range(1, len(prices)):
            max_curr_diff += prices[i] - prices[i - 1]
            max_curr_diff = max(0, max_curr_diff)
            max_profit = max(max_curr_diff, max_profit)
        return max_profit

    def one_pass_soln(self, prices: List[int]) -> int:
        """
        The maximum profit = max - min such that min index < max index
        """
        min_value = float("inf")
        max_profit = 0
        for val in prices:
            if val < min_value:
                min_value = val
            else:
                max_profit = max(val - min_value, max_profit)
        return max_profit

    def brute_force_soln(self, prices: List[int]) -> int:
        """
        Brute Force solution

        Runtime: O(n^2)
        Space: O(1)
        """
        res = 0
        for left in range(len(prices) - 1):
            for right in range(left + 1, len(prices)):
                res = max(prices[right] - prices[left], res)
        return res

# @lc code=end


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)
    print(Solution().maxProfit([7, 6, 4, 3, 1]), 0)
